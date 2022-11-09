"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jiri Steif
email: jiristeif@seznam.cz
discord: Caddi#3130
"""

from task_template import TEXTS as texts

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

user = input("Enter your username: ").lower()
password = input("Enter your password: ")

if user in users.keys() and password == users.get(user):
    print(f"Login successful, welcome {user}!")
else:
    print("Unknown user")
    exit()

