from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_option)

driver.get("https://www.youtube.com/")

search_area = driver.find_element(by=By.NAME, value="search_query")
time.sleep(3)

search_area.send_keys("Vinland Saga Season 3")
time.sleep(3)

search_btn = driver.find_element(by=By.CLASS_NAME, value="ytSearchboxComponentSearchButton")
search_btn.click()
