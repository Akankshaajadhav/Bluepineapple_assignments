from database import connect_to_db

def search_book():
    search_name = input("Enter the title of the book to search: ")
    
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM book WHERE name LIKE %s", ('%' + search_name + '%',))
    books = cursor.fetchall()

    if books:
        for book in books:
            print(f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Price: {book[3]}")
    else:
        print("Book not found.")
    
    cursor.close()
    conn.close()
