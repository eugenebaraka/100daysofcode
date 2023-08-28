#Password Generator Project
import random
import string
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))
  password_list.append(random.choice(numbers))
  password_list.append(random.choice(symbols))

random.shuffle(password_list)

# for char in range(nr_numbers):
#   password_list += random.choice(numbers)
# print(password_list)

# random.shuffle(password_list)
#
password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

import string

# print(list(string.ascii_letters))
# print(random.choice(string.digits))
# print(string.punctuation)


import keyring

print(keyring.get_password("https://www.spotify.com", "eugene.baraka@mail.mcgill.ca"))
