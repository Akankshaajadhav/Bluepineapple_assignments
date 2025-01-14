from book_data import books
# from add_book import count,add_book

def view_books():
    if not books:
        print("No books are added.")
        return

    print("Book list is:")
    for book in books:
        print(f"ID: {book['id']}, Title: {book['name']}, Author: {book['author']}, Price: {book['price']}")
