from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def get_articles_count():
    chrome_driver_path = "/Users/ania/development/chromedriver"
    service = Service(executable_path=chrome_driver_path)
    
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://en.wikipedia.org/wiki/Main_Page")
        articles_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text

    return articles_count

if __name__ == "__main__":
    articles_count = get_articles_count()
    print(articles_count)