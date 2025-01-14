from book_data import books

def search_book():
    search_name = input("Enter the title of the book to search: ")
    
    flag=0
    for book in books:
        if book["name"].lower() == search_name.lower():
            print(f"Book Found: ID: {book['id']}, Title: {book['name']}, Author: {book['author']}, Price: {book['price']}")
            flag=1
            break

    if flag==0:
        print("Book not found.")
