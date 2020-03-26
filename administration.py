"""Define a set of functions related to registration."""
from getpass import getpass

from config import registered_users, registered_users_lower
from nav import show_welcome_menu

def register_user():
    """Build a new user profile and store it into registered users dictionary."""
    print("\n---- Subscription menu ----")
    user_name_verified = False
    while not user_name_verified:
        user_name = input("Enter a new user name: ")
        user_name = user_name.strip()
        """
        Enforce that user name is unique based on a case sensitive test
        before registering the account.
        """
        if user_name.lower() in registered_users_lower:
            print(f"Sorry, {user_name} is already registered. Try a new one.")
            continue

        if len(user_name) < 2:
            print("Sorry, your user's name must be at least 2 characters long.")
            continue

        pass_word = getpass("Enter a new pass word: ")
        pass_word = pass_word.strip()

        """Add a registering user into the user's database."""
        if len(pass_word) > 6:
            """SHOULD shield from SQL injection"""
            registered_users[user_name] = pass_word
            print(f"Thanks {user_name}, you have been successfully registered.")
            """
            The user is registered and authenticated.
            He is also redirected to main menu.
            """
            user_name_verified = True
            welcome_menu_active = False
            options_menu_active = True
        else:
            print("Please enter a pass word at least 6 characters long"
            " to ensure your account's safety.")


def authenticate_user():
    """Authenticate a user who is logging in the user's database."""
    print("\n---- Authentication menu ----")
    user_name = input("Enter your name: ")
    user_name = user_name.strip()
    pass_word = getpass("Enter your pass word: ")
    """
    The authentication test must ensure that the visitor cannot know
    whether the login and/or the pass word are wrong to prevent a
    brute-force attack on one field
    """
    for login_user_name, login_pass_word in registered_users.items():
        if (login_user_name == user_name) and (login_pass_word == pass_word):
            print(f"\nWelcome {user_name}.")

        # else:
        #   # Executed twice because of the conditional test composed of 2 boolean expressions
        #   print("Authentication has failed. Try again.")


def welcome_visitor():
    """Define a welcoming menu to deal with visitors."""
    welcome_menu_active = True
    options_menu_active = False
    while welcome_menu_active:
        show_welcome_menu()
        try:
            option = int(input("\nSelect an option: "))
        except ValueError:
            print("Please enter a numerical value!")
        # Catch a ValueError = invalid literal for int() with base 10: '<user_input>'
        else:
            if option == 1:
                authenticate_user()
                welcome_menu_active = False
                options_menu_active = True

            elif option == 2:
                register_user()
                welcome_menu_active = False
                options_menu_active = True

            elif option == 3:
                print("Program exit.")
                welcome_menu_active = False

            else:
                print("Option unknown. Select an existing option.")