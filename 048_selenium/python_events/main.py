from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def fetch_events():
    chrome_driver_path = "/Users/ania/development/chromedriver"
    service = Service(executable_path=chrome_driver_path)
    
    with webdriver.Chrome(service=service) as driver:
        driver.get("http://www.python.org")
        events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
        
        event_list = [
            {
                'time': event.find_element(By.TAG_NAME, 'time').get_attribute('datetime'),
                'name': event.find_element(By.TAG_NAME, 'a').text
            }
            for event in events
        ]
        
    return event_list

if __name__ == "__main__":
    events = fetch_events()
    for event in events:
        print(event)