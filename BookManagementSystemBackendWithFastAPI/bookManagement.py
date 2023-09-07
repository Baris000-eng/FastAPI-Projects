from http.client import HTTPException

from fastapi import Body
from fastapi import FastAPI

# %20 stands for a space.

# Swagger UI in FastAPI allows use to see the HTTP requests we send to the endpoints and the results of these attempts.

# The use of async in Python allows you to create functions that can
# operate concurrently, which means they can perform tasks simultaneously
# without blocking the execution of your program. This concurrency is especially
# valuable when dealing with I/O-bound operations like network requests, file reading/writing,
# or database queries, as it enables your program to remain responsive and efficient by
# overlapping the execution of tasks.


# to run this fastapi app, use following: uvicorn bookManagement:fast_api_app --reload
fast_api_app = FastAPI()

# to observe the SwaggerUI, use following: http://127.0.0.1:8000/docs

# status code = 200 means that everything was successful.
list_of_books = [
    {'title': 'Title 1', 'author': 'Author 1', 'category': 'science'},
    {'title': 'Title 2', 'author': 'Author 1', 'category': 'history'},
    {'title': 'Title 3', 'author': 'Author 3', 'category': 'action'},
    {'title': 'Title 4', 'author': 'Author 4', 'category': 'math'},
    {'title': 'Title 5', 'author': 'Author 5', 'category': 'math'},
    {'title': 'Title 6', 'author': 'Author 6', 'category': 'physics'}
]


@fast_api_app.get("/")
async def first_api():
    return {"message": "Hello Baris!"}


# async keyword for function definitions is optional
@fast_api_app.get("/hello-world")
def hello_world():
    return "Hello World"


# an endpoint definition for retrieving the book names.
@fast_api_app.get("/books")
def books():
    return list_of_books


# loop all through the list of books
# when there is a match between the book title we pass as a dynamic parameter and
# a book title in the book list, then it will return the corresponding book instance.
@fast_api_app.get("/book/{book_title}")
async def read_book(book_title: str):
    for book in list_of_books:
        if book.get('title').lower() == book_title.lower():
            return book


# FastAPI treats the same function definitions but different implementations from top to bottom
# in the order of definition.

# In the endpoint of the below function, an example of static path
# parameter passing to the endpoint can be seen.
@fast_api_app.get("/books/mybook")
async def read_books():
    favorite_book_dict = {'book_title': 'My favorite book!'}
    return favorite_book_dict


# dynamic path parameter passing to the endpoint
@fast_api_app.get("/books/{dynamic_param}")
async def read_books(dynamic_param: str):
    dynamic_param_dict = {'dynamic_param': dynamic_param}
    return dynamic_param_dict


# Query Parameters

# Query Parameters are request parameters that have been attached after a "?"
# Query Parameters have name=value pairs

# Examples of Query Parameters:

# 127.0.0.1:8000/books?category=math
# 127.0.0.1:8000/books?category=science

# Usage of a Single Query Parameter in an Endpoint
@fast_api_app.get("/books/")
async def read_category_by_query(category: str):
    book_list_to_return = list()
    for book in list_of_books:
        if book.get("category").lower() == category.lower():
            book_list_to_return.append(book)
    return book_list_to_return


# Usage of Multiple Query Parameters in an Endpoint
@fast_api_app.get("/getBooksByAuthorAndCategory/")
async def read_author_and_category_by_query(author_name: str, category: str):
    books_list_to_return = []
    for book in list_of_books:
        if book.get("author").lower() == author_name.lower() and book.get("category").lower() == category.lower():
            books_list_to_return.append(book)

    return books_list_to_return


# Simultaneous Usage of Query Parameters and Path Parameters in a FastAPI Endpoint
@fast_api_app.get("/getBooksByTitleAndCategory/{book_title}")
async def read_title_and_category_by_query(book_title: str, category: str):
    returned_books = list()
    for book in list_of_books:
        if book.get("title").lower() == book_title.lower() and \
                book.get("category").lower() == category.lower():
            returned_books.append(book)
    return returned_books


############################################################################################
# GET HTTP Request Method cannot have a body.
# However, POST HTTP Request Method can have a body.

# POST HTTP Request Method
# POST HTTP Request Method is used to create data.
# POST can have a body that has additional information which GET does not have.

# This function gets the request body as the parameter.
@fast_api_app.post("/books/create_book")
async def create_book(new_book=Body()):
    list_of_books.append(new_book)


############################################################################################
# PUT HTTP Request Method
# PUT HTTP Request Method is used to update data.
# PUT can have a body that has additional information (like POST) which GET does not have.
@fast_api_app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for j in range(0, len(list_of_books)):
        book = list_of_books[j]
        if book.get("title").lower() == updated_book.get("title").lower():
            list_of_books[j] = updated_book


############################################################################################
# DELETE HTTP Request Method
# DELETE HTTP Request Method is used to delete data.
# In the above function, book_title is a path parameter.
@fast_api_app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for x in range(0, len(list_of_books)):
        if list_of_books[x].get("title").lower() == book_title.lower():
            list_of_books.pop(x)
            break


##############################################################################################
# PATCH HTTP Request Method
# PATCH applies partial modifications to a data/resource.

# This endpoint allows partial modifications to a book's attributes, such as author and category.
# It takes a book_title as a path parameter to identify the book to update.
# The updated_attributes parameter in the request body should be a JSON object containing the attributes to modify.
# If the book with the specified title is found, it updates the provided attributes and returns the updated book.
# If the book is not found, it raises an HTTP 404 error to indicate that the book does not exist.

# Given the book title, it updates author and category attributes which are the other ones.
@fast_api_app.patch("/books/update_book/{book_title}")
async def update_book_attributes(book_title: str, updated_attributes=Body()):
    for book in list_of_books:
        if book.get("title").lower() == book_title.lower():
            for key, value in updated_attributes.items():
                if key in book:
                    book[key] = value
            return book

    raise HTTPException(status_code=404, detail="Book not found")


###############################################################################################

# The below function is a GET HTTP request method
# It gets the book records by the author name
# In the below function, the utilized endpoint takes the author name as a path parameter.
@fast_api_app.get("/getBooksByAuthor/{author_name}")
async def getBooksByAuthor(author_name: str):
    books_lst = list()
    for book in list_of_books:
        if book.get("author").lower() == author_name.lower():
            books_lst.append(book)
    return books_lst
###############################################################################################

