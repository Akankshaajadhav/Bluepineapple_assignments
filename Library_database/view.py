from database import connect_to_db

def view_books():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()

    if books:
        for book in books:
            print(f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Price: {book[3]}")
    else:
        print("No books available.")

    cursor.close()
    conn.close()
