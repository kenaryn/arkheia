#!/usr/bin/env python3.8
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
