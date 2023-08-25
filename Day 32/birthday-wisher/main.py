import pandas
import datetime as dt

# read in data
birthdays_data = pandas.read_csv("birthdays.csv")
print(birthdays_data["day"])
today = dt.datetime.now().day

# has_birthday_today = birthdays_data[birthdays_data["day"] == today]
# print(has_birthday_today)

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




