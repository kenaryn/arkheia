"""Define a set of classes representing a book."""

class Book:
    """A simple class book."""
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def read_book(self):
        """Show information about a single book."""
        print(f"Title: {self.title.capitalize()}")
        print(f"Author: {self.author.title()}")
        print(f"Publisher: {self.publisher.title()}")
        print(f"Year: {self.year}")

    def remove_book(self, title):
        """Remove a title-related book from the library."""
        file_path = 'text_files/'
        with open({file_path}book) as file_object:
            library = file_object.readlines()
            for book in library:
                if title in books:
                    books.remove(title)
                else:
                print(f"'{title.capitalize()}' does not exist in your library.")