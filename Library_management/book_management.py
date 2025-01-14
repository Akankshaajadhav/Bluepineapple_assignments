from add_book import add_book
from allocate_book import allocate_book
from search_book import search_book
from view_books import view_books
from deallocate_book import deallocate_book

def main():
    while True:
        print("This is Book Management System.")
        print("1. Add book")
        print("2. Allocate book")
        print("3. Search book")
        print("4. View all books")
        print("5. Deallocate book")
        print("6. Exit")

        choice = int(input("Choose your option: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            allocate_book()
        elif choice == 3:
            search_book()
        elif choice == 4:
            view_books()
        elif choice == 5:
            deallocate_book()
        elif choice == 6:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
