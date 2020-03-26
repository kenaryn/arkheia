"""Define all functions related to keep the records."""
from config import books
from display import get_formatted_name

def show_logs():
    """Show the last three added books."""

    print("\nLogs:\nThe three most recent books:")
    if len(books) == 0:
        print("There is currently no log because no book has been added yet.")
    else:
        last_three_books = books[-3:]
        last_three_books.reverse()
        for book in last_three_books:
            book = get_formatted_name(book)
            print(f" - {book}")
        print(f"\nThe library contains {len(books)} books.")
    print()