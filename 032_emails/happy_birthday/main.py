import smtplib
import os
import pandas as pd
import random
import datetime as dt
from settings import EMAIL_USERNAME, EMAIL_PASSWORD, FROM_EMAIL

def main():
    for index, row in get_today_birthdays().iterrows():
        name = row["name"]
        email = row["email"]
        letter_template = get_random_letter_template()
        letter = letter_template.replace("[NAME]", name)
        send_email(email, "Happy Birthday!", letter)

def get_today_birthdays():
    try:
        today = dt.datetime.now()
        birthdays = pd.read_csv("birthdays.csv")
        today_birthdays = birthdays[(birthdays["month"] == today.month) & (birthdays["day"] == today.day)]
        return today_birthdays
    except FileNotFoundError:
        return "birthdays.csv file not found."

def get_random_letter_template(directory="letter_templates"):
    try:
        files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        if not files:
            raise FileNotFoundError("No files found in the directory.")
        random_file = random.choice(files)
        with open(os.path.join(directory, random_file), 'r') as file:
            template = file.read()
        return template
    except FileNotFoundError as e:
        return str(e)


def send_email(to_email, subject, body):
    with smtplib.SMTP("mail.smtp2go.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_USERNAME, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{body}"
        )

if __name__ == "__main__":
    main()