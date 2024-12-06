from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.page_load_strategy = 'normal'

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    # Wait for and select language
    language = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )
    language.click()

    # Wait for the game to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
    cookie = driver.find_element(By.ID, "bigCookie")

    
    while True:
        cookie.click()

        try:
            items = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
            for item in reversed(items): 
                item.click()
        except Exception as e:
            print("No products available to purchase:", str(e))

        if keyboard.is_pressed("q"):
            print("Exiting the script...")
            break

        time.sleep(0.1)  # Prevent overloading the CPU

finally:
    time.sleep(2)
    driver.quit()
