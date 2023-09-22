#  SQLAlchemy
#  SQLAlchemy uses ORM. It is an ORM-based Python library which enables
#  us to interact with the relational databases such as Sqlite.
#  To install SQLAlchemy, we can use the following: pip install sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from DatabaseConstants import DatabaseConstants

engine = create_engine(DatabaseConstants.MYSQL_DATABASE_URL)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database_object = declarative_base()
