from database import connect_to_db

def deallocate_book():
    book_id = int(input("Enter the ID of the book to deallocate: "))

    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM book WHERE id = %s AND allocated = TRUE", (book_id,))
    book = cursor.fetchone()

    if book:
        cursor.execute("UPDATE book SET allocated = FALSE WHERE id = %s", (book_id,))
        conn.commit()
        print(f"Book with ID {book_id} has been deallocated!")
    else:
        print(f"Book with ID {book_id} is either not found or not allocated.")

    cursor.close()
    conn.close()
