"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jiri Steif
email: jiristeif@seznam.cz
discord: Caddi#3130
"""

from task_template import TEXTS

# defining users and their passwords
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# getting the user's username and password
user = input("Enter your username: ").lower()
password = input("Enter your password: ")

# checking if entered username is defined in users
# checking if entered password is a valid value for the user
if user in users.keys() and password == users.get(user):
    print(f"Login successful, welcome {user}!")
else:
    # if not -> inform and end
    print("Unknown user")
    exit()

# print out samples of texts for user to select
for i,text in enumerate(TEXTS):
    print(f"Text nr. {i}: {TEXTS[i][:20]} ...")

# getting the text selection from user
text_selection = input("Choose one of the texts (by it's number) to be processed: ")

# validate the user text selection
if text_selection.isnumeric() and 0 <= int(text_selection) < len(TEXTS):
    text_selection_index = int(text_selection)
    print(f"Selected text: nr. {text_selection_index}: {TEXTS[text_selection_index][:20]} ...")
else:
    # invalid input -> inform user and exit
    print("Invalid text choice")
    exit()

text_split = TEXTS[text_selection_index].split()

print(text_split)