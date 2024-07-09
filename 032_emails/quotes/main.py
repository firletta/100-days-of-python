import smtplib
import random
import datetime as dt
from settings import EMAIL_USERNAME, EMAIL_PASSWORD, TO_EMAIL, FROM_EMAIL

def main():
    if today_is_tuesday():
        quote = random_quote()
        send_email(TO_EMAIL, "Tuesday Quote", quote)

def today_is_tuesday():
    now = dt.datetime.now()
    return now.weekday() == 1

def random_quote():
    with open("quotes.txt") as file:
        quotes = file.readlines()
    return random.choice(quotes)

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