from fastapi import FastAPI, Body, Path, Query, HTTPException
from Book import Book
from starlette import status
from BookRequest import BookRequest
import HttpErrorMessages

app = FastAPI()
# The following command will run this FastAPI project: uvicorn BooksProject:app --reload

http_error_messages = HttpErrorMessages()

books_list = [
    Book(1, "Introduction to Programming with Python!", "MikeTeeve", "A great book!", 4, 2010),
    Book(2, "Introduction to Backend Web Development with FastAPI", "ElonMusk!",
         "A super book with enough coding exercises !", 3, 2021),
    Book(3, "Introduction to Java Programming and OOP", "MarkZuckerberg",
         "It is a beneficial guide in your journey of learning Java and OOP", 5, 2017)
]

# HTTP Request Methods

# CRUD         HTTP Request Methods

# Create ====> POST
# Read ======> GET
# Update ====> PUT
# Delete ====> DELETE

"""FastAPI is now compatible with both Pydantic v1 and Pydantic v2.

Based on how new the version of FastAPI you are using, there could be small method name changes.


The three biggest are:

.dict() function is now renamed to .model_dump()

schema_extra function within a Config class is now renamed to json_schema_extra

Optional variables need a =None example: id: Optional[int] = None"""


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_book_records():
    return books_list


# 201: Created is suitable for POST requests. When an entity is created
# with a POST request, then the "201: Created" status code is utilized.
@app.post("/createBook", status_code=status.HTTP_201_CREATED)
async def create_book(book_request=Body()):
    books_list.append(book_request)


# Pydantics

# Pydantics is a Python library that is used for data parsing, data modelling, and data validation.
# Moreover, it involves an efficient error handling mechanism.

# Pydantics is commonly used as a resource for data validation and how to handle data coming
# to our FastAPI application.

# Pydantics enables us to apply data validation on each variable. We can use Field library of Pydantics module to do so.

# Body does not allow us """"""""""""""""""""""""""""""""""""""""""""""""""""to do any data validation.


# Passing book request object as the request body enables us to apply field validation.
@app.post("/createBookWithValidation")
async def create_book_with_data_validation(book_request: BookRequest):
    print(type(book_request))  # <class 'BookRequest.BookRequest'>
    # Double asteriks (**) operator will pass the key&value from the BookRequest into the Book() constructor.
    new_book = Book(**book_request.model_dump())  # converting the book request to the Book object.
    books_list.append(findBookIdWithTernaryOperation(new_book))


# In Pydantic V1
# dict()
# schema_extra function in Config class

# In Pydantic V2
# dict() -----> model_dump()
# schema_extra() ----> json_schema_extra()
# Optional variables started to need a = None
# Ex: id: Optional[int] = None


def findBookId(book: Book):
    """
    If the book record is to be the first one to be added to the book list (i.e. if the length of the
    list of books is 0 before the addition of the Book record to the list), then set the id of the book
    record as 1. Otherwise, set the id of the book record to be one more than the id of the last book
    record in the list of books.
    """
    if len(books_list) == 0:
        book.book_id = 1
    else:
        book.book_id = books_list[len(books_list) - 1].book_id + 1

    return book


def findBookIdWithTernaryOperation(book: Book):
    book.book_id = 1 if len(books_list) == 0 else books_list[len(books_list) - 1].book_id + 1
    return book


# Path(gt=-1) data validation makes sure that the path parameter of book_id
# can be greater than or equal to 0.
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def readBooksByBookId(book_id: int = Path(gt=-1)):
    for book in books_list:
        if book.book_id == book_id:
            return book

    raise HTTPException(status_code=404, detail=HttpErrorMessages.book_record_not_found(book_id))


# Reading books by their ratings
# In this function, book_rating is a query parameter.

# Query(gt=0, lt=6) data validation makes sure that the book_rating
# passed as a query parameter should be greater than 0 and less than 6 (start = 1, end = 5)
@app.get("/books/", status_code=status.HTTP_200_OK)
async def readBooksByRating(book_rating: int = Query(gt=0, lt=6)):
    returned_books = list()
    for book in books_list:
        if book.book_rating == book_rating:
            returned_books.append(book)

    return returned_books


# PUT HTTP Request Method
@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_updated = False
    for a in range(0, len(books_list)):
        if books_list[a].book_id == book.book_id:
            books_list[a] = book
            book_updated = True

    if not book_updated:
        raise HTTPException(status_code=404, detail=HttpErrorMessages.book_record_not_found_for_update())


# PUT HTTP Request Method


# DELETE HTTP Request Method
# In the below function, the path parameter called book_id
# is specified to be greater than or equal to 0 by using
# Path(ge=0).
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(ge=0)):
    bookDeleted = False
    for a in range(0, len(books_list)):
        book_record = books_list[a]
        if book_record.book_id == book_id:
            books_list.remove(book_record)
            bookDeleted = True
            break

    if not bookDeleted:
        raise HTTPException(status_code=404,
                            detail=HttpErrorMessages.book_record_not_found_for_deletion(book_id))


# DELETE HTTP Request Method


# Filtering the books by their published years
# GET HTTP Request Method

# Query(gt=1998, lt=2068) data validation makes sure that the published year passed as
# a query parameter should be greater than 1998 and less than 2068 (start = 1999 , end = 2067)
@app.get("/filterBooks/", status_code=status.HTTP_200_OK)
async def filterBooksByPublishedYear(published_year: int = Query(gt=1998, lt=2068)):
    filtered_books = []
    for book in books_list:
        if book.published_year == published_year:
            filtered_books.append(book)

    return filtered_books
# GET HTTP Request Method
# Filtering the books by their published years
