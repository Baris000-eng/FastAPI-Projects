import datetime
from http.client import HTTPException
from typing import Annotated
from Token import Token

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from jose import JWTError, jwt
from fastapi import HTTPException

import PasswordHashingService
from CreateUserRequest import CreateUserRequest
# from PostgreSQLDatabaseConnection import local_session # for postgresql db
# from MySQLDatabaseConnection import local_session  # for mysql db
from SQLiteDatabaseConnection import local_session
from DbUsersTableModel import Users
from PasswordHashingService import hashPassword
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta

# To enter the sqlite3 database called todosapp.db, you can use the below command:
# sqlite3 todosapp.db

#   API Router class under the Python's fastapi library allows us to be able to route
#   from TodoMain.py file to the UserAuthentication.py file.
apiRouter = APIRouter(
    prefix='/auth',
    tags=['auth']
)

# Division of the application with a new title of auth is provided by the above
# specification of tags parameter in the APIRouter object. Under the title called
# 'auth', the prefix tag will put 'auth' to the beginning of each endpoint in this
# UserAuthentication.py file. In other words, each endpoint will start with 'auth'
# after specifying the prefix parameter in the APIRouter object as above.

# The secret and the algorithm will work together to add a
# signature to the JWT to make sure that JWT is secured and
# authorized.
SECRET_KEY = "a18383838GGjfewjfk..!!,00099xz00ecvbh70*936"
SIGNING_AND_VERIFICATION_ALGORITHM = 'HS256'
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/usertoken')


# Yield keyword in Python means that only the code
# prior to and including the yield statement before
# sending a response.

# Since the yield keyword is used, the 'finally' block
# will not run in the below function until all the
# database session information is retrieved.
def obtain_database():
    database = local_session()
    try:
        yield database  # Here, the execution of the function is temporarily suspended.
    finally:
        database.close()


database_dependency = Annotated[Session, Depends(obtain_database)]
form_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]


def create_access_token(username: str, user_id: int, user_role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': user_role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=SIGNING_AND_VERIFICATION_ALGORITHM)


def authenticate_user(username: str, password: str, database):
    user = database.query(Users).filter(Users.username == username).first()
    print(user)
    print(password)
    print(user.hashed_pwd)

    # Check if user exists, hashed password exists, and password verification succeeds.
    # In password verification, bcrypt automatically hashes the user-typed password and
    # checks whether it matches with the one existing in the database.
    if user and user.hashed_pwd and PasswordHashingService.bcrypt_context.verify(password, user.hashed_pwd):
        return user, True

    return None, False


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        jwt_payload = jwt.decode(token, SECRET_KEY, algorithms=[SIGNING_AND_VERIFICATION_ALGORITHM])
        username: str = jwt_payload.get('sub')
        user_id: str = jwt_payload.get('id')
        user_role: str = jwt_payload.get('role')
        if user_id is None or username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User validation cannot be done"
            )
        return {"username": username, "id": user_id, "user_role": user_role}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User validation cannot be done"
        )


# The below function is an example of writing an ORM-based query to get
# all the user records in the database.
@apiRouter.get("/auth/")
async def get_user(database: database_dependency):
    return database.query(Users).all()


# In the below function named 'create_user', the database dependency is
# injected into the function.
@apiRouter.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(database: database_dependency,
                      createUserRequest: CreateUserRequest):
    user_model = Users(
        email=createUserRequest.email,
        username=createUserRequest.username,
        initial_name=createUserRequest.first_name,
        surname=createUserRequest.surname,
        user_role=createUserRequest.role,
        hashed_pwd=hashPassword(createUserRequest.password),
        is_active=True,
        phone_number=createUserRequest.phone_number
    )

    database.add(user_model)
    database.commit()


@apiRouter.post("/usertoken", response_model=Token)
async def login_for_access_token(form_data: form_dependency,
                                 database: database_dependency):
    user_authenticated = authenticate_user(form_data.username, form_data.password, database)
    user_object = user_authenticated[0]
    is_authenticated = user_authenticated[1]
    if not is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User validation cannot be done.'
        )

    token = create_access_token(user_object.username, user_object.user_id, user_object.user_role, timedelta(minutes=30))
    return {"token_type": "bearer", "access_token": token}
