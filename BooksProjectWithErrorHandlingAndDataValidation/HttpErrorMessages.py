def book_record_not_found_for_deletion(book_id: int):
    return f"The book record with ID {book_id} does not exist and cannot be deleted!"


def book_record_not_found_for_update():
    return "The book record to be updated cannot be found!"


def book_record_not_found(book_id: int):
    return f"The book record with the book ID {book_id} cannot be found!"
