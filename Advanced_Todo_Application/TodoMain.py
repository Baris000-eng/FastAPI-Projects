from fastapi import FastAPI

from routers import UserAuthentication
from routers import Todos

from DatabaseConnection import engine
import DbTodosTableModel
import DbUsersTableModel

fastapi_app = FastAPI()
DbTodosTableModel.database_object.metadata.create_all(bind=engine)
DbUsersTableModel.database_object.metadata.create_all(bind=engine)

fastapi_app.include_router(UserAuthentication.apiRouter)
fastapi_app.include_router(Todos.apiRouter)
