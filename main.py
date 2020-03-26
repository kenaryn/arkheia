#!/usr/bin/env python3.7
"""
Build a user profile allowing to build a library.
Each user is able to add, remove, edit or search among the books.
"""
from getpass import getpass

from administration import register_user, authenticate_user, welcome_visitor
from library import search_book, edit_book, show_library, add_book, remove_book, explore_library
from log import show_logs
from config import registered_users, registered_users_lower, books

welcome_visitor()
explore_library()


"""
TODO:
1. Add a access' level feature to implement a safety policy (e.g. only List/Search, can_edit = False)
2. if 3 failed attempts, suggest to the user a subscription (i.d. yes/no question to pursue authentication
or switch to subscription option)
3. Allow a admin to create multiple libraries.
4. A user can access to multiple librairies.
"""