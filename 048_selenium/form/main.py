from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def fill_in_form(driver, first_name, last_name, email):
    driver.get("http://secure-retreat-92358.herokuapp.com/")
    
    driver.find_element(By.NAME, "fName").send_keys(first_name)
    driver.find_element(By.NAME, "lName").send_keys(last_name)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.TAG_NAME, "button").click()

def create_driver(chrome_driver_path):
    service = Service(executable_path=chrome_driver_path)
    return webdriver.Chrome(service=service)

if __name__ == "__main__":
    chrome_driver_path = "/Users/ania/development/chromedriver"
    driver = create_driver(chrome_driver_path)
    
    try:
        fill_in_form(driver, "Megan", "Smith", "megan@smith.com")
    finally:
        driver.quit()