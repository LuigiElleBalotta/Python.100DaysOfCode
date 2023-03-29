# 1. Send an email with smtplib
import smtplib
#
# my_email = input("What is your email? ")
# password = "uckiqrqdjuhtiobb"
# email_target = input("Who is the target of the email? ")
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # Encrypts the connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=email_target, msg="Subject:Hello\n\nThis is the body of my email.")

# 2. Handle dates with datetime library
import datetime as dt

# now = dt.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1996, month=10, day=6)
# print(date_of_birth)

# 3. Send motivational quotes on mondays via email
import random

now = dt.datetime.now()
if now.weekday() == 0:
    my_email = input("What is your email? ")
    password = "uckiqrqdjuhtiobb"

    chosen_quote = None
    try:
        with open("quotes.txt") as file:
            quotes = file.readlines()
            chosen_quote = random.choice(quotes)
    except FileNotFoundError:
        print("File not found")
    else:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            print("Sending email...")
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Motivational quote\n\n{chosen_quote}")
else:
    print("Not sending email since is not monday...")

