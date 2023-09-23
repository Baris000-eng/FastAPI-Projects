# from MySQLDatabaseConnection import database_object
from sqlalchemy import Integer, Column, ForeignKey, Boolean, String

# from PostgreSQLDatabaseConnection import database_object
from SQLiteDatabaseConnection import database_object


class Todos(database_object):
    __tablename__ = 'todos'

    todo_id = Column(Integer, primary_key=True, index=True)
    todo_is_complete = Column(Boolean, default=False)
    todo_title = Column(String)
    todo_description = Column(String)
    todo_priority = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.user_id"))
