from fastapi import FastAPI

from routers import UserAuthentication
from routers import Admin
from routers import Todos
from routers import Users

from SQLiteDatabaseConnection import engine
import DbTodosTableModel
import DbUsersTableModel

fastapi_app = FastAPI()
DbTodosTableModel.database_object.metadata.create_all(bind=engine)
DbUsersTableModel.database_object.metadata.create_all(bind=engine)

# Registering the applications routers.
fastapi_app.include_router(UserAuthentication.apiRouter)
fastapi_app.include_router(Todos.apiRouter)
fastapi_app.include_router(Admin.apiRouter)
fastapi_app.include_router(Users.apiRouter)
