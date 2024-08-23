# Homework 9 - Library Management System

from inventory import *
from borrow import *
from return_book import *


def main():
    inventory = ["1984", "Harry Potter - The Half-Blood Prince", "Animal Farm"]
    borrowed_books = []

    _user_in_library = True

    while _user_in_library:
        print("\n")
        print('*' * 31)
        print("Library Management System")
        print('*' * 31)
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. Add a Book to Inventory")
        print("4. Remove a Book from Inventory")
        print("5. View Inventory")
        print("6. View Borrowed Books")
        print("7. Exit")
        print('*' * 31)

        try:
            _user_choice = int(input("\nEnter your choice (1-7): "))
            print()

            if _user_choice == 1:
                book_title = input("Enter the Book Title you want to Borrow: ")
                borrow_book(inventory, borrowed_books, book_title)

            elif _user_choice == 2:
                book_title = input("Enter the Book Title you want to Return: ")
                return_a_book(inventory, borrowed_books, book_title)

            elif _user_choice == 3:
                book_title = input("Enter the Book Title you want to Add: ")
                add_book(inventory, book_title)

            elif _user_choice == 4:
                book_title = input("Enter the Book Title you want to Remove: ")
                remove_book(inventory, book_title)

            elif _user_choice == 5:
                print("\nBooks in Inventory:")
                for book in inventory:
                    print(f"- {book}")

            elif _user_choice == 6:
                print("\nBorrowed Books:")
                for book in borrowed_books:
                    print(f"- {book}")

            elif _user_choice == 7:
                _user_in_library = False
                print("Thank you for using the Library Management System!")

            else:
                print("\nInvalid choice! Please select a Valid Option.")

        except ValueError:
            print("\nPlease enter a valid number.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
