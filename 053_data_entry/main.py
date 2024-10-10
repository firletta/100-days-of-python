from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



def scrape_listings():
    base_url = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/bialystok/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    listings = soup.select(".css-1g5933j")

    data = []
    for listing in listings:
        price = listing.select_one(".css-13afqrm").text
        address = listing.select_one(".css-1mwdrlh").text.split(" - ")[0]
        url = listing.select_one(".css-z3gu2d").get("href")

        data.append({
            "price": price,
            "address": address,
            "url": url
        })

    return data


def create_driver():
    chrome_driver_path = "/Users/ania/development/chromedriver"
    service = Service(executable_path=chrome_driver_path)
    return webdriver.Chrome(service=service)


def fill_in_form(driver, price, address, url):
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLScC2LdE4xX_9Hh-NpVYxcKg0ZZkGc993ToWm151ATHO6KiNYQ/viewform?usp=sf_link")
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price)
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address)
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(url)
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div').click()


def main():
    listings = scrape_listings()
    driver = create_driver()

    for listing in listings:
        fill_in_form(driver=driver, price=listing["price"], address=listing["address"], url=listing["url"])

    driver.quit()

if __name__ == "__main__":
    main()



