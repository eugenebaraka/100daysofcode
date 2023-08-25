import random
import csv

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace",
         "Hannah", "Isaac", "Jack", "Adam", "Bobby", "Ange", "Muswati"]
email = "eugenebaraka@gmail.com"
def generate_birthday():
    year = random.randint(1965, 2004)
    month = random.randint(1, 12)
    day = random.randint(1, 28)

    return year, month, day


for _ in range(200):
    try:
        birthdays = open("birthdays.csv", "a")
    except FileNotFoundError:
        with open("birthdays.csv", "w") as birthdays:
            file = csv.writer(birthdays)
            file.writerow("name, email, year, month, day")
    else:
        random_name = random.choice(names)
        dates = generate_birthday()
        birthdays.write(f"{random_name}, {email}, "
                        f"{dates[0]}, {dates[1]}, {dates[2]}\n")
        birthdays.close()
