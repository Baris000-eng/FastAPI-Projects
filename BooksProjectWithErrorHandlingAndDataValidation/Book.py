class Book:
    book_id: int
    title: str
    author: str
    description: str
    rating: int
    published_year: int

    def __init__(self, book_id, book_title, author, book_description, book_rating, published_year):
        self.book_id = book_id
        self.book_title = book_title
        self.author = author
        self.book_description = book_description
        self.book_rating = book_rating
        self.published_year = published_year



