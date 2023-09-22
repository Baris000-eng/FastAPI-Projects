# Production Databases

# Both MySQL and PostgreSQL are used widely in the enterprise applications.

# Production DBMS vs SQLite

# ----------------------------#

# SQLite

# SQLite3 aims to provide local data storage for the individual applications and devices.

# For the most small/medium-scale applications, SQLite3 will work very well.

# SQLite3 emphasizes economy, efficiency, and simplicity.

# SQLite3 focuses on different concepts than a production Database Management System.

# Production DBMS

# The production database management systems such as MySQL and PostgreSQL focus on
# concurrency, scalability, and control.

# If the application is going to have a lot of users (ex: 10s of thosands of users),
# then it may be a good idea to switch to a production DBMS.

# Production Database Management Systems (Production DBMS)

# SQLite3 runs in-memory or local disk. This allows the
# development of a SQlite3 data to be easy.

# SQLite3 is a serverless and self-contained database.

# Production database management systems run on their own server and port.
# You need to make sure that the database is running,

# For the application deployment:

# * (SQLite3) For deployment, an SQLite3 database and the application itself can be deployed.
# * (Production DBMS) For deployment, we will need to deploy the database seperate from the
# application.


# ---------------------------------------------------#

# RDBMS = Relational Database Management Systems
# What is PostgreSQL ?
# PostgreSQL is a production-ready database.
# PostgreSQL is an open-source relational database management system.
# PostgreSQL is a secure database.
# PostgreSQL requires a server.
# PostgreSQL is a highly scalable database.

# In PostgreSQL, SERIAL means the field property of being auto-incremented.
