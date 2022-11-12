"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jiri Steif
email: jiristeif (zavinac) seznam.cz
discord: Caddi#3130
"""

from task_template import TEXTS


def tisk_oddelovace(sirka, znak):
    """print out a separator - made as function
    in case of future upgrade to something more fancy"""
    print(sirka * znak)


# defining users and their passwords
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

oddelovac = "-"
sirka_radku = 40

# getting the user's username and password
user = input("Enter your username: ").lower()
password = input("Enter your password: ")

# checking if entered username is defined in users
# checking if entered password is a valid value for the user
if user in users.keys() and password == users.get(user):
    tisk_oddelovace(oddelovac, sirka_radku)
    print(f"Login successful, welcome {user}!")
else:
    # if not -> inform and end
    print("Unknown user. Terminating..")
    exit()

tisk_oddelovace(oddelovac, sirka_radku)

# print out samples of texts for user to select
for i, text in enumerate(TEXTS):
    print(f"Text nr. {i}: {TEXTS[i][:20]} ...")

tisk_oddelovace(oddelovac, sirka_radku)

# getting the text selection from user
text_selection = input("Enter a number btw. 0 and 2 to select: ")

tisk_oddelovace(oddelovac, sirka_radku)

# validate the user text selection
text_selection_index = 0
if text_selection.isnumeric() and 0 <= int(text_selection) < len(TEXTS):
    text_selection_index = int(text_selection)
    # print(f"Selected text: nr. {text_selection_index}: {TEXTS[text_selection_index][:20]} ...")
else:
    # invalid input -> inform user and exit
    print("Invalid text choice. Terminating..")
    exit()

# split the chosen text into a list of words
text_split = TEXTS[text_selection_index].split()

# "clean" the words -> remove unwanted characters
text_split_cleared = []
for word in text_split:
    text_split_cleared.append(word.strip(".,:;?!\n"))

number_of_words = len(text_split_cleared)  # calculate the number of words
number_of_words_with_titlecase = 0
number_of_words_with_upper = 0
number_of_words_with_lower = 0
number_of_numeric_words = 0
sum_of_all_numbers = 0
lenghts_of_words = dict()

for word in text_split_cleared:
    if 64 < ord(word[0]) < 91:  # check if first letter is a capital letter
        number_of_words_with_titlecase += 1

    if word.isupper() and word.isalpha():  # check if whole word is in uppercase
        number_of_words_with_upper += 1

    if word.islower() and word.isalpha():  # check if whole word is in lowercase
        number_of_words_with_lower += 1

    if word.isnumeric():  # check if word is numeric and add it to the total if it is
        number_of_numeric_words += 1
        sum_of_all_numbers += int(word)

    # put the length of word into the dictionary of lengths and amounts
    # if the length is already a key -> increment by 1
    if lenghts_of_words.get(len(word), 0) == 0:
        lenghts_of_words[len(word)] = 1
    else:
        lenghts_of_words[len(word)] += 1

# print out all the values
print(f"There are {number_of_words} words in the selected text.")
print(f"There are {number_of_words_with_titlecase} titlecase words.")
print(f"There are {number_of_words_with_upper} uppercase words.")
print(f"There are {number_of_words_with_lower} lowercase words.")
print(f"There are {number_of_numeric_words} numeric strings.")
print(f"The sum of all the numbers is {sum_of_all_numbers}")

tisk_oddelovace(oddelovac, sirka_radku)

print(f"LEN|{'OCCURENCES': ^20} |NR.")
tisk_oddelovace(oddelovac, sirka_radku)

sorted_keys = sorted(list(lenghts_of_words.keys()))

for key in sorted_keys:
    print(f"{key: >3}|{lenghts_of_words.get(key)*'*': <20} |{lenghts_of_words.get(key)}")
