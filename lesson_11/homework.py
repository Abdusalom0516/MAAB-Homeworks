# Task 1
# 1. **Parse the HTML File**:
#    - Load the `weather.html` file using BeautifulSoup and extract the weather forecast details.

# 2. **Display Weather Data**:
#    - Print the **day**, **temperature**, and **condition** for each entry in the forecast.

# 3. **Find Specific Data**:
#    - Identify and print the day(s) with:
#      - The highest temperature.
#      - The "Sunny" condition.

# 4. **Calculate Average Temperature**:
#    - Compute and print the **average temperature** for the week.


from bs4 import BeautifulSoup

html_code = ""
# 1.
with open("weather.html", "r") as f:
    html_code = f.read()

soup = BeautifulSoup(html_code, "html.parser")

all_weather_data = soup.find_all("tr")[1:]
max_temperature = -999
temperatures = []

# 2.
for value in all_weather_data:
    children = value.find_all("td")

    temperature = int(str(children[1].text).replace("°C", ""))
    temperatures.append(temperature)

    if temperature > max_temperature:
        max_temperature = temperature

    print(f"{children[0].text}, {children[1].text}, {children[2].text}.")

print("---------------------------")


# 3.
print("Highest Tempreature")
for value in all_weather_data:
    children = value.find_all("td")
    temperature = int(str(children[1].text).replace("°C", ""))

    if temperature == max_temperature:
        print(f"{children[0].text}, {children[1].text}, {children[2].text}.")

print("---------------------------")


# 4.
print("Average Temperature of the Week")
print(f"{sum(temperatures) / len(temperatures)}°C")




# Task 3
import json
print("------------------------------")
#  1. **Navigate to the Website:**
#    - Visit the [Demoblaze homepage](https://www.demoblaze.com/).
#    - Click on the **Laptops** section to view the list of available laptops.

# 2. **Navigate to the Next Page:**
#    - After reaching the Laptops section, locate and click the **Next** button to navigate to the next page of laptop listings.

# 3. **Data to Scrape:**
#    For each laptop on the page, scrape the following details:
#    - **Laptop Name**
#    - **Price**
#    - **Description**

# 4. **Data Storage:**
#    - Save the extracted information in a structured **JSON format** with fields like:
#      json
#      [
#        {
#          "name": "Laptop Name",
#          "price": "Laptop Price",
#          "description": "Laptop Description"
#        },
#        ...
#      ]

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time # I am gonna use it to add waiting time to make it clear to myself whta is happening in my code.
import os

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

# 1.
driver.get("https://www.demoblaze.com/")


laptop_categories = driver.find_elements(by=By.ID, value="itemc")

laptop_categories[1].click()
time.sleep(3)

next_btn = driver.find_element(by=By.ID, value="next2")
next_btn.click()
time.sleep(3)

laptops = driver.find_elements(by=By.CLASS_NAME, value="card-block")

json_laptops = []


for laptop in laptops:
    split_list = laptop.text.split(f"\n")

    json_laptops.append({ "name": split_list[0],
         "price": split_list[1],
         "description":split_list[2]})


with open("laptops.json", "a") as f:
        json.dump(json_laptops, f, indent=4)






