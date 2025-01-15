from database import connect_to_db

def allocate_book():
    book_id = int(input("Enter the ID of the book to allocate: "))

    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM book WHERE id = %s AND allocated = FALSE", (book_id,))
    book = cursor.fetchone()

    if book:
        cursor.execute("UPDATE book SET allocated = TRUE WHERE id = %s", (book_id,))
        conn.commit()
        print(f"Book with ID {book_id} has been allocated!")
    else:
        print(f"Book with ID {book_id} is not found or already allocated.")

    cursor.close()
    conn.close()
