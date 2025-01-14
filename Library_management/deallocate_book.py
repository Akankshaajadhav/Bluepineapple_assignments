from book_data import borrowed_books

def deallocate_book():
    book_id = int(input("Enter the ID of the book to deallocate: "))

    # Check if the book is currently allocated
    if book_id in borrowed_books:
        user_id = borrowed_books.pop(book_id)  # Remove the allocation
        print(f"Book ID {book_id} returned by User ID {user_id}.")
    else:
        print("The book is not currently allocated.")
