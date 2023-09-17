# Inserting to the database table todos
# We can achieve the insertion in the following way:

# INSERT INTO todos(title, description, priority, complete)
# VALUES ("Go to gym", "1 hour cardio in gym to stay healthy", 4, False)


# SELECT SQL QUERIES

# The below command selects all columns and rows from the database table called 'todos'.
# SELECT * FROM todos;

# The below command selects the titles of the todos.
# SELECT todo_title FROM todos;

# The below command selects the descriptions of the todos.
# SELECT todo_description FROM todos;

# AN SQL QUERY EXAMPLE OF SELECTING TWO COLUMNS FROM THE DB TABLE called 'todos'
# The below command selects both the titles and descriptions of the todos.
# SELECT todo_title, todo_description FROM todos;

# AN SQL QUERY EXAMPLE OF SELECTING THREE COLUMNS FROM THE DB TABLE called 'todos'
# The below command selects the titles, descriptions, and priorities of the todos.
# SELECT todo_title, todo_description, todo_priority

# WHERE SQL QUERIES (WHERE CLAUSE IN SQL)

# The below command will select all todos from the table called todos
# where the priority is 3.
# SELECT * FROM todos WHERE priority=3;

# The below command will select all rows and columns of the todos #
# where the title of the todo is 'Go to gym' #
# SELECT * FROM todos WHERE todo_title = "Go to gym"

# UPDATE SQL QUERIES (UPDATE CLAUSE IN SQL)

# The below command will change the completeness status of the
# todo with id being equal to 3 to True

# UPDATE todos SET todo_is_complete=True WHERE todo_id = 3

# DELETE SQL QUERIES (DELETE CLAUSE IN SQL)

# The best way to delete from a database table (todos in this case)
# is with the usage of primary key.

# The below command will delete the todos from the db table called 'todos'
# where the todo id is 1.
# DELETE FROM todos WHERE todo_id = 1

# Deletion without primary key

# The below command will delete incomplete todos from the db table called 'todos':
# DELETE FROM todos WHERE complete = 0;
