from book_data import books

def add_book():
    # global count
    book = {}
    book["id"] = len(books) + 1
    book["name"] = input("Enter book name: ")
    book["author"] = input("Enter author name: ")
    book["price"] = int(input("Enter book price: "))

    books.append(book)
    # count += 1
    print("Book added successfully!")
