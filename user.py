# The import is currently inacessible because log.py is in a parent directory.
from logs import update_logs
from config import libraries
"""Define a class representing a user."""

class User():
    """A simple user class."""
    def __init__(self, first_name, last_name, location, field, age=''):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.field = field
        self.login_attempts = 0
        if age:
            self.age = age

    def increment_login_attempts(self):
        """Add 1 to the login attempt's value."""
        self.login_attempts += 1

    def get_login_attempts(self):
        """Check the numbers of loggin attempts."""
        return self.login_attempts

class Admin(User):
    """Define a administrator with higher privileges."""
    def __init__(self, first_name, last_name, location, field, age='')
        super().__init__(first_name, last_name, location, field, age)
        self.can_create_library = True
        self.can_remove_user = True
        self.can_destroy_library = True

    def create_library(self, library_name):
        """Build a new empty library."""
        # Insert a try-except-else block here.
        new_library = input("Enter a name for a new library: ")
        # try:
            # new_library = Library(f"'{new_library}'")
        if new_library not in libraries:
            libraries.append(new_library)
            update_logs()
        elif new_library in libraries:
            print(f"{new_library} already exists.")

    def explore_library(self, library_name):
        """Gain access to all library's functions."""
