""" * This Module is for Returning a Books * """


def return_a_book(inventory, borrowed_books, book_title):
    if book_title in borrowed_books:
        borrowed_books.remove(book_title)
        inventory.append(book_title)
        print(f"\nYou have returned '{book_title}'.")
    else:
        print(f"\n'{book_title}' is not in your borrowed books list.")
