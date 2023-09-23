from fastapi import HTTPException, Path, Query, APIRouter
from fastapi import Depends  # for dependency injection
from starlette import status
from typing import Annotated
from sqlalchemy.orm import Session
from DbTodosTableModel import Todos
from SQLiteDatabaseConnection import local_session
# from MySQLDatabaseConnection import local_session
from DbUsersTableModel import Users
from UserVerification import UserVerification
from .UserAuthentication import get_current_user
from TodoRequest import TodoRequest
from passlib.context import CryptContext

apiRouter = APIRouter(
    prefix='/user',
    tags=['user']
)


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
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@apiRouter.get('/', status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, database: database_dependency):
    print(user)
    if user is None:
        raise HTTPException(status_code=401, detail='User authentication cannot be done.')

    return database.query(Users).filter(Users.user_id == user.get('id')).first()


@apiRouter.put('/changePassword', status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, database: database_dependency, user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail='User authentication is failed.')

    user_model = database.query(Users).filter(Users.user_id == user.get('id')).first()

    if not bcrypt_context.verify(user_verification.password, user_model.hashed_pwd):
        raise HTTPException(status_code=401, detail='Error on password updating.')

    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    print(user_model.hashed_password)
    database.add(user_model)
    database.commit()


@apiRouter.put("/updatePhoneNumber/{phone_number}", status_code=status.HTTP_204_NO_CONTENT)
async def update_phone_number(user: user_dependency, database: database_dependency,
                              phone_number: str = Path()):
    if user is None:
        raise HTTPException(status_code=401, detail='User authentication is failed.')

    user_model = database.query(Users).filter(Users.user_id == user.get('id')).first()

    user_model.phone_number = phone_number

    database.add(user_model)
    database.commit()
