from book_data import books, borrowed_books

def allocate_book():
    book_id = int(input("Enter the ID of the book to allocate: "))
    user_id = input("Enter the User ID: ")

    # Check if the book exists
    for book in books:
        if book["id"] == book_id:
            # Check if the book is already allocated
            if book_id in borrowed_books:
                print(f"Book ID {book_id} is already allocated to User ID {borrowed_books[book_id]}.")
                return

            # Allocate the book
            borrowed_books[book_id] = user_id
            print(f"Book ID {book_id} ('{book['name']}') allocated to User ID {user_id}.")
            return

    print("Book not found.")
