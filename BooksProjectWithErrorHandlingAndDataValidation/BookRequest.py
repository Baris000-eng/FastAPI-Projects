from pydantic import BaseModel, Field
from typing import Optional


# BaseModel is the core class in Pydantics. By using BaseModel,
# Pydantics automatically generates the default validation for
# the class fields based on their types.

# Field class under the Pydantics module enables us to set additional limitations to the class fields.
class BookRequest(BaseModel):
    # book_id can also be specified as an int (book_id: int). However, then, the book_id cannot take a None value.
    # This is opposite to the case of book_id being Optional.

    book_id: Optional[int] = None  # When we pass the book id as Optional, it means that the book id can either
    # take a value or be null.
    book_title: str = Field(min_length=15)
    author: str = Field(min_length=12)
    book_description: str = Field(min_length=25, max_length=85)
    book_rating: int = Field(gt=0, lt=6)
    published_year: int = Field(gt=1998, lt=2068)
    """In Pydantic, the Config class is used to configure various settings and behaviors for a Pydantic model.
    It allows you to customize how Pydantic validates and processes data in your models.You can define a Config 
    class as an inner class within your Pydantic model to specify these settings."""

    """
    Q: What is the purpose of class Config within our class BookRequest(BaseModel)?
    A: To create a more descriptive request within our Swagger Documentation.
    """
    class Config:
        json_schema_extra = {
            'example': {
                'title': 'Harry Potter',
                'author': 'J.K. Rowling',
                'description': 'A new description of a Harry Potter book',
                'rating': 5,
                'published_year': 2028
            }
        }


