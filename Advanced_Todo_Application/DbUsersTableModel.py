from SQLiteDatabaseConnection import database_object
from sqlalchemy import Integer, Column, Boolean, String


# To verify a user, instead of comparing the actual passwords
# we compare the hashes of the passwords.

class Users(database_object):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)  # username is specified as unique here.
    email = Column(String, unique=True)  # email is specified as unique here.
    initial_name = Column(String)
    surname = Column(String)
    hashed_pwd = Column(String)  # hashed password
    user_role = Column(String)
    is_active = Column(Boolean, default=True)  # The default value given to the is_active column is True.
