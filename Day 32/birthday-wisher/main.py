import random
import smtplib
import pandas
import datetime as dt
import keyring

email = "eugenebaraka@gmail.com"
password = keyring.get_password("100daysofcode", email)
def send_email(message:str, to_addrs:str):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=to_addrs, msg=message)

# read in data
birthdays_data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now().day
this_month = dt.datetime.now().month
has_birthday_today = birthdays_data[(birthdays_data.day == today) &
                                    (birthdays_data.month == this_month)]

for friend in has_birthday_today["name"]:
    # pick random letter
    letter_num = random.randint(1, 3)
    selected_letter = "letter_" + str(letter_num) + ".txt"
    with open(f"./letter_templates/{selected_letter}", "r") as birthday_letter:
        letter = birthday_letter.read()
        new_letter = letter.replace("[NAME]", friend)
        new_letter = new_letter.replace("Angela", "Eugene")

        # get email
        to_email = has_birthday_today[has_birthday_today.name == friend]["email"]
        # send message
        send_email(message=f"Subject: HAPPY BIRTHDAY!!!\n\n{new_letter}",
                   to_addrs=to_email)






# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




