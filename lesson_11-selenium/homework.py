# Task 1
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


# Task 2
print("------------------------------")

import sqlite3
import requests
from bs4 import BeautifulSoup
import sqlite3

value = requests.get("https://realpython.github.io/fake-jobs/")

soup = BeautifulSoup(value.text, "html.parser")

card_contents = soup.find_all("div", class_="card-content")

jobs = []
for elem in card_contents:
    media_content = elem.find("div", class_="media-content")
    content = elem.find("div", class_="content")
    all_links = elem.find_all("a")
    job_title = media_content.find("h2").text
    company_name = media_content.find("h3", class_="subtitle").text
    location = str(content.find("p", class_="location").text).strip()
    application = all_links[1].get("href")
    jobs.append((job_title, company_name, location, application))

    with sqlite3.connect("jobs.db") as connect:
        cursor = connect.cursor()

        create_table_query = "CREATE TABLE IF NOT EXISTS jobs(job_title TEXT, company_name TEXT, location TEXT, application_link TEXT, UNIQUE(job_title, company_name, location))"
        cursor.execute(create_table_query)

        values_question_mark = ", ".join(["?"] * 4)
        insert_values_query = f"""
            INSERT INTO jobs VALUES ({values_question_mark})
            ON CONFLICT(job_title, company_name, location)
            DO UPDATE SET application_link = excluded.application_link;
        """
        cursor.executemany(insert_values_query, jobs)


def get_jobs_by_location(location: str):
    with sqlite3.connect("jobs.db") as connect:
        cursor = connect.cursor()

        jobs_by_locations_query = f"SELECT * FROM jobs WHERE location = {location}"
        data = cursor.execute(jobs_by_locations_query).fetchall()
        print(data)


def get_jobs_by_company_name(company_name: str):
    with sqlite3.connect("jobs.db") as connect:
        cursor = connect.cursor()

        jobs_by_company_name_query = f"SELECT * FROM jobs WHERE company_name = {company_name}"
        data = cursor.execute(jobs_by_company_name_query).fetchall()
        print(data)





# Task 3
import json
print("------------------------------")

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






