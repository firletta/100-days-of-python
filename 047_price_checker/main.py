import requests
from bs4 import BeautifulSoup
import smtplib
from config import EMAIL_USERNAME, EMAIL_PASSWORD, TO_EMAIL, FROM_EMAIL, URL, DESIRED_PRICE


def scrape_price(url: str) -> float:
    """
    Scrapes the price of a product from a given URL.

    Args:
        url (str): The URL of the product.

    Returns:
        float: The price of the product.
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    price_element = soup.select_one(".price")
    price_text = price_element.get_text(strip=True).replace("zł", "").replace(",", ".")
    return float(price_text)

def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Sends an email with the specified subject and body.

    Args:
        to_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.
    """
    msg = f"Subject:{subject}\n\n{body}".encode('utf-8')
    with smtplib.SMTP("mail.smtp2go.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_USERNAME, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=to_email,
            msg=msg
        )

def main() -> None:
    """
    Main function to scrape the product price and send an email alert if the price is below the desired threshold.
    """
    try:
        price = scrape_price(URL)
        if price <= DESIRED_PRICE:
            send_email(
                to_email=TO_EMAIL,
                subject="Price Alert!",
                body=f"„Bez alko i dragów jestem nudna“ is now {price} zł. Buy now! {URL}"
            )
            print("Email sent.")
        else:
            print(f"The current price is {price} zł, which is above the desired price of {DESIRED_PRICE} zł.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()