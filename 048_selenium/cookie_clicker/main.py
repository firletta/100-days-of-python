import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_driver(chrome_driver_path):
    service = Service(executable_path=chrome_driver_path)
    return webdriver.Chrome(service=service)

def cookie_clicker(driver, duration_seconds):
    driver.get("http://orteil.dashnet.org/experiments/cookie/")
    time.sleep(2)
    
    end_time = time.time() + duration_seconds
    cookie = driver.find_element(By.ID, "cookie")
    
    while time.time() < end_time:
        cookie.click()
        
        items = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for item in items[::-1]:
            try:
                if item.text.split(" - ")[0] in ["Cursor", "Grandma", "Factory", "Mine", "Shipment", "Alchemy lab", "Portal", "Time machine"]:
                    item.click()
            except StaleElementReferenceException:
                logger.warning("Stale element reference, retrying...")
                items = driver.find_elements(By.CSS_SELECTOR, "#store div")

if __name__ == "__main__":
    chrome_driver_path = "/Users/ania/development/chromedriver"
    
    driver = create_driver(chrome_driver_path)
    try:
        cookie_clicker(driver, 5*60)
        input("Press Enter to close the browser...")
    finally:
        driver.quit()