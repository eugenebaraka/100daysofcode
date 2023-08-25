import random
import smtplib
import datetime as dt
import keyring

with open("data/quotes.txt", "r") as quotes:
    all_quotes = quotes.readlines()


email = "eugenebaraka@gmail.com"
password = keyring.get_password("100daysofcode", email)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)

    # if day is Thursday send a random quote to my email
    now = dt.datetime.now()

    if now.weekday() == 3:
        today_quote = random.choice(all_quotes)
        message = f"Subject: A little motivation for you\n\n{today_quote}"
        connection.sendmail(from_addr=email, to_addrs=email, msg=message)
