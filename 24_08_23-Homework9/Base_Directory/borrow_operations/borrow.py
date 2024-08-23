""" * This Module is for Borrowing Books * """


def borrow_book(inventory, borrowed_books, book_title):
    if book_title in inventory:
        inventory.remove(book_title)
        borrowed_books.append(book_title)
        print(f"\nYou have borrowed '{book_title}'.")
    else:
        if book_title in borrowed_books:
            print(f"\nYou've already borrowed, '{book_title}' from the Library.")
        else:
            print(f"\nSorry, '{book_title}' is not available in the inventory.")
