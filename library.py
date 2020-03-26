"""Define all functions related to business logic."""
from getpass import getpass

from config import books
from display import get_formatted_name
from nav import show_options_menu

def search_book():
    """Search for a book and return its title if found in the library."""
    book = input("Enter the name of the book you search for: ")
    book = book.lower().strip()
    if book in books:
        print(book.capitalize())
    else:
        print(f"'{book.capitalize()}' is not found in the library.")


def edit_book():
    """Search for a book and allow the user to rename it."""
    book = input("Enter the title of the book you want to edit: ")
    book = book.lower().strip()
    if book in books:
        new_title = input("Type a new title: ")
        new_title = new_title.lower().strip()
        """
        Store the index's searched element via its name to replace
        the corresponding occurence.
        """
        index_searched = books.index(book)
        books[index_searched] = new_title
        print(f"'{book.capitalize()}' has been renamed into '{new_title.capitalize()}'.")
    else:
        print(f"'{book.capitalize()}' is not found in the library.")


def show_library():
    """Show all books' titles included in the library."""
    if len(books) == 0:
        print("\nThe current library is empty.")
    elif len(books) == 1:
        print(books[0].title())
        print("The library contains only 1 book.")
    elif len(books) > 1:
        print("Here are listed the books included in the library:")
        print()
        sorted(books)

        i = 1
        for book in books:
            book = get_formatted_name(book)
            print(f" {i}. {book}")
            i += 1
    print()


def add_book():
    """Allow the user to add 1 or n book in the library."""
    print("--- Adding a new book ---")
    print("(Press 'q' to quit this submenu)")
    while True:
        new_book = input("\nEnter a new title's book: ")
        if new_book == 'q':
            print("Returning to the main menu.")
            print()
            break

        if new_book in books:
            print("This book already exists in the library.")
        else:
            new_book = new_book.lower().strip()
            books.append(new_book)
            print(f"'{new_book.capitalize()}' has been successfully added.")


def remove_book():
    """Search for a book in order to remove it from the library based on its title."""
    print("--- Removing a book ---")
    print("(Press 'q' to quit this submenu)")
    while True:
        book_to_remove = input("\nEnter the title's book to remove: ")
        if book_to_remove == 'q':
            break

        book_to_remove = book_to_remove.lower().strip()
        if book_to_remove in books:
            books.remove(book_to_remove)
            book_to_remove = get_formatted_name(book_to_remove)
            print(f"{book_to_remove} has been removed.")
        else:
            print(f"'{book_to_remove}' does not exist in the library.")


def explore_library():
    """Define a menu to administrative the whole library."""
    while options_menu_active:
        show_options_menu()
        option = int(input("\nSelect a menu: "))
        if option == 1:
            show_library()
        elif option == 2:
            add_book()
        elif option == 3:
            remove_book()
        elif option == 4:
            search_book()
        elif option == 5:
            edit_book()
        elif option == 7:
            show_logs()
        elif option == 8:
            print("Program exit.")
            options_menu_active = False
        else:
            print("Menu unknown. Select a existing menu.")

class Library:
    """Build a simple library."""
    def __init__(self, name):
        self.name = name
        self.books = Book()