from fastapi import FastAPI, HTTPException, Path, Query
from fastapi import Depends  # for dependency injection
from starlette import status

from todo_request import TodoRequest
from database_connection import engine
from database_connection import local_session
import database_table_models
from typing import Annotated
from sqlalchemy.orm import Session
from database_table_models import Todos

fastapi_app = FastAPI()
database_table_models.database_object.metadata.create_all(bind=engine)


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


# 'Depends' import from FastAPI represents the dependency injection.
# In the below function, Depends(obtain_database) means that
# this function depends on the database session instance being
# created. This database session is injected to the below function
# as an instance called 'db'.
@fastapi_app.get("/", status_code=status.HTTP_200_OK)
async def read_todos(database: database_dependency):
    return database.query(Todos).all()


# The below function gets the todos that have the
# todo id same with the one passed as a path parameter.

"""When a request to the below endpoint is successfully processed, FastAPI will automatically 
respond with a JSON response and a status code of 200 OK by default, indicating that 
the request was successful. This default HTTP response is set with the status_code parameter."""


@fastapi_app.get("/getTodo/{todo_id}", status_code=status.HTTP_200_OK)
async def getTodoById(database: database_dependency, todo_id: int = Path(gt=0)):
    todo_model = database.query(Todos).filter(
        Todos.todo_id == todo_id).first()  # get the first record where todo ids match. Due to the uniqueness of todo ids, using first() will be fine here.
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo is not found")
    return todo_model


@fastapi_app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(database: database_dependency, todoRequest: TodoRequest):
    todo_object_model = Todos(**todoRequest.model_dump())
    database.add(todo_object_model)
    database.commit()  # this makes the above addition operation automatically happen.


###################################################################################################
# HTTP PUT Request Method

# In the below HTTP PUT request function, the todo_is is passed as a query parameter.
@fastapi_app.put("/todo/", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(database: database_dependency, todo_request: TodoRequest, todo_id: int = Query(description="The ID of the todo item to update", gt=0)):
    todo_object_model = database.query(Todos).filter(Todos.todo_id == todo_id).first()
    if todo_object_model is None:
        raise HTTPException(status_code=404, detail='Todo cannot be found in the db table called todos')

    todo_object_model.todo_title = todo_request.todo_title
    todo_object_model.todo_description = todo_request.todo_description
    todo_object_model.todo_priority = todo_request.todo_priority
    todo_object_model.todo_is_complete = todo_request.todo_is_complete

    database.add(todo_object_model)
    database.commit()


# HTTP PUT Request Method
###################################################################################################

###################################################################################################
# HTTP DELETE Request Method

# In the below HTTP DELETE request function, the todo_is is passed as a path parameter.
@fastapi_app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(database: database_dependency, todo_id: int = Path(gt=0)):
    todo_object_model = database.query(Todos).filter(Todos.todo_id == todo_id).first()
    if todo_object_model is None:
        raise HTTPException(status_code=404, detail='Todo cannot be found in the db table called todos')
    database.query(Todos).filter(Todos.todo_id == todo_id).delete()

    database.commit()

# HTTP DELETE Request Method
###################################################################################################
