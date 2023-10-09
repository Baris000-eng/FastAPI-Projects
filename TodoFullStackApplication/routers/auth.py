import sys

from fastapi import Depends, Form, HTTPException, status, APIRouter, Response, Request
from fastapi.openapi.models import Response
from pydantic import BaseModel
from typing import Optional
from starlette.responses import RedirectResponse

import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routers.loginForm import LoginForm

SECRET_KEY = "KlgH6AzYDeZeGwD288to79I3vTHT8wp7"
ALGORITHM = "HS256"

# Specifying the place where the Jinja2 templates live
templates = Jinja2Templates(directory="templates")


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

models.Base.metadata.create_all(bind=engine)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authorized"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, db):
    user = db.query(models.Users) \
        .filter(models.Users.username == username) \
        .first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int,
                        expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


# token: str = Depends(oauth2_bearer)#
async def get_current_user(request: Request):
    try:
        token = request.cookies.get('access_token')  # obtaining the access token from the cookie
        print("The access token is: " + str(token) + "")
        if token is None:
            return None
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise user_exception()
        return {"username": username, "id": user_id}
    except JWTError:
        return None


@router.post("/create/user")
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = models.Users()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name

    hash_password = get_password_hash(create_user.password)

    create_user_model.hashed_password = hash_password
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()


@router.post("/token")
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return False
    token_expires = timedelta(minutes=50)
    token = create_access_token(user.username,
                                user.id,
                                expires_delta=token_expires)

    response.set_cookie(key="access_token", value=token, httponly=True)
    return True


@router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("registerpage.html", {"request": request})


@router.post("/register", response_class=HTMLResponse)
async def register_user(
    request: Request,
    email: str = Form(...),
    username: str = Form(...),
    firstname: str = Form(...),
    lastname: str = Form(...),
    password: str = Form(...),
    verification_password: str = Form(...),
    database: Session = Depends(get_db)
):
    first_valid = database.query(models.Users).filter(models.Users.username == username).first()
    second_valid = database.query(models.Users).filter(models.Users.email == email).first()

    print(first_valid)
    print(second_valid)
    print(password)
    print(verification_password)

    print(first_valid is not None)
    print(second_valid is not None)
    print(password != verification_password)

    if (first_valid is not None) or (second_valid is not None) or (password != verification_password):
        failure_reg = "Invalid registration!"
        return templates.TemplateResponse("registerpage.html", {"request": request, "msg": failure_reg})

    user_model = models.Users()
    user_model.username = username
    user_model.first_name = firstname
    user_model.last_name = lastname
    user_model.email = email

    password_hash = get_password_hash(password=password)
    user_model.hashed_password = password_hash

    user_model.is_active = True
    database.add(user_model)
    database.commit()
    successful_reg = "User is successfully created!"
    return templates.TemplateResponse("loginpage.html", {"request": request, "msg": successful_reg})


@router.get("/logout")
async def logout(request: Request):
    message = "Logout is successful"
    response = templates.TemplateResponse("loginpage.html", {"request": request, "msg": message})
    response.delete_cookie(key="access_token")  # delete the cookie from the html template response
    return response  # return the html template response where the cookie is deleted


# Endpoint: http://127.0.0.1:8000/auth/
@router.get("/", response_class=HTMLResponse)
async def authenticationPage(request: Request):
    return templates.TemplateResponse("loginpage.html", {"request": request})


@router.post("/", response_class=HTMLResponse)
async def login(request: Request, database: Session = Depends(get_db)):
    try:
        form = LoginForm(request)
        await form.create_oauth_form()
        response = RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)
        validate_user_cookie = await login_for_access_token(response=response, db=database, form_data=form)

        if not validate_user_cookie:
            message = "Incorrect Username or Password!"
            return templates.TemplateResponse("loginpage.html", {"request": request, "msg": message})

        return response
    except HTTPException:
        message = "Unknown Error!"
        return templates.TemplateResponse("loginpage.html", {"request": request, "msg": message})


# Exceptions

def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_exception_response


def user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credentials_exception
