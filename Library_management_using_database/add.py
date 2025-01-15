from database import connect_to_db

def add_book():
    book_name = input("Enter book name: ")
    author = input("Enter author name: ")
    price = input("Enter book price: ")

    conn=connect_to_db()
    cursor=conn.cursor()

    cursor.execute('''
        INSERT INTO book (name, author, price)
        VALUES (%s, %s, %s)
    ''', (book_name, author, price))
    
    conn.commit()
    print("Book added successfully!")
    
    cursor.close()
    conn.close()
