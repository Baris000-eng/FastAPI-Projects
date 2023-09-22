from fastapi import HTTPException, Path, Query, APIRouter
from fastapi import Depends  # for dependency injection
from starlette import status
from typing import Annotated
from sqlalchemy.orm import Session
from DbTodosTableModel import Todos
from SQLiteDatabaseConnection import local_session
from .UserAuthentication import get_current_user
from TodoRequest import TodoRequest

apiRouter = APIRouter(
    prefix='/admin',
    tags=['admin']
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


@apiRouter.delete("/getTodo", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, database: database_dependency, todo_id: int = Query(gt=0)):
    if user.get('user_role') != 'admin' or user is None:
        raise HTTPException(status_code=401, detail='User authentication cannot be done.')

    todo_model = database.query(Todos).filter(Todos.todo_id == Todos.todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo is not found!')

    database.query(Todos).filter(Todos.todo_id == todo_id).delete()
    database.commit()


@apiRouter.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency,
                   database: database_dependency):
    if user.get('user_role') != 'admin' or (user is None):
        raise HTTPException(status_code=401, detail="User authentication cannot be done.")
    return database.query(Todos).all()
