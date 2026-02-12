# Task 1.
# data = ["10", "25", "x", "42", "", "17", "error", "99"]

# valid_numbers = []
# sum_valid_numbers = 0
# avg = 0


# for elem in data:
#     try:
#         valid_numbers.append(int(elem))
#         sum_valid_numbers += valid_numbers[-1]
#     except:
#         pass

# avg = sum_valid_numbers / len(valid_numbers)


# print(valid_numbers)
# print(sum_valid_numbers)
# print(avg)


# Task 2.
# def get_max(numbers_list: list[int]) -> int:
#     max_number =  numbers_list[0]
#     for elem in numbers_list:
#         if elem > max_number:
#             max_number = elem
#     return max_number

# def get_min(numbers_list: list[int]) -> int:
#     min_number = numbers_list[0]
#     for elem in numbers_list:
#         if min_number > elem:
#             min_number = elem
#     return min_number


# def get_avg(numbers_list: list[int]) -> float:
#     numbers_sum = sum(numbers_list)
#     return numbers_sum / len(numbers_list)


# numbers_list = [15, 12, 8, 10]

# print(get_max(numbers_list=numbers_list))
# print(get_min(numbers_list=numbers_list))
# print(get_avg(numbers_list=numbers_list))


# Task 3.
# class Employee:
#     name: str
#     salary: float

#     def __init__(self, *, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def __str__(self):
#         return f"Employee(name: {self.name}, salary: {self.salary})"

#     def give_raise(self, *, percent) -> None:
#         self.salary = self.salary + (self.salary * (percent / 100))

#     def display_info(self):
#         print(self)

#     @property
#     def info(self):
#         return "Shit"
    



# employee = Employee(name="Abdusalom", salary=2500)
# employee.display_info()
# employee.give_raise(percent=10)
# employee.display_info()
# print(employee.info)


# Task 4.
# import numpy as np

# array = np.array([12, 45, 7, 33, 56, 21, 90, 3])

# numbers_greater_than_30 = array[array > 30]
# numbers_between_10_and_50 = array[(array >= 10) & (array <= 50)]

# print(numbers_greater_than_30)
# print(numbers_between_10_and_50)



# Task 5.
# import numpy as np

# array_4x4 = np.random.randint(1, 11, (4, 4))
# row_means = array_4x4.mean(axis=1)
# column_sums = array_4x4.sum(axis=0)
# max_number = array_4x4.max()

# print(array_4x4)
# print(row_means)
# print(column_sums)
# print(max_number)



# Task 6.
# import requests
# import csv

# BASE_URL = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(BASE_URL)

# if response.status_code == 200:
#     response = response.json()
#     user_data = []
#     for user_info in response:
#         name = user_info["name"]
#         email = user_info["email"]
#         city = user_info["address"]["city"]
#         user_data.append({"name": name, "email": email, "city": city})

#     with open("user_data.csv", "w") as f:
#         writer = csv.DictWriter(f=f, delimiter=",", fieldnames=["name", "email", "city"])
#         writer.writeheader()
#         writer.writerows(user_data)

#     print(user_data)
# else:
#     print(f"Failed to get! {response.status_code}.")


# Task 7.
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import sqlite3

# BASE_URL = "https://jovonnalondon.com/collections/all-2"
# response = requests.get(BASE_URL)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     products = []

#     all_products = soup.find_all("div", class_="block-inner-inner")
#     for product in all_products:
#         product_img = "https:"+product.find_all("img", class_="rimage__image")[-1].get("src")
#         product_title = product.find("div", class_="product-block__title").text
#         product_price = str(product.find("div", class_="product-price").text).strip()

#         products.append([product_img, product_title, product_price])

#     df = pd.DataFrame(data=products, columns=["product_img", "product_title", "product_price"])

#     connection = sqlite3.connect("products.db")
#     df.to_sql("products", con=connection, if_exists="replace",)

# else:
#     print(f"Failed to get! {response.status_code}.")



# Task 8.
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# chrome_options = Options()

# # chrome_options.add_argument("--headless") # Works but does not open the browser
# chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://google.com/")

# search_button = driver.find_element(by=By.ID, value="APjFqb")

# search_button.send_keys("Vinland Saga Season 2", Keys.ENTER)



# Task 9
# Working with SQLLite & Pandas
# import sqlite3
# import pandas as pd

# with sqlite3.connect("company.db") as connection:
#     cursor = connection.cursor()

#     table_create_query = """
#         DROP TABLE IF EXISTS employees;

#         CREATE TABLE employees(
#             id integer,
#             name text,
#             department text,
#             salary integer
#         );

#         INSERT INTO employees
#         VALUES
#         (1, 'Abdusalom', 'IT', 2500),
#         (2, 'Abdulmalik', 'Accounting', 1800),
#         (3, 'Malika', 'HR', 2000),
#         (4, 'Fotima', 'IT', 2100),
#         (5, 'Muhammad', 'Management', 2000);
#     """

#     cursor.executescript(table_create_query)


#     select_query = """
#         SELECT * FROM employees
#         WHERE salary > 2000
#     """
#     df = pd.read_sql(select_query, con=connection)
#     print(df)



# Task 10.
# Matplotlib
# from matplotlib import pyplot as plt

# departments = ["IT", "HR", "Finance", "Sales"]
# salaries = [80000, 50000, 60000, 70000]

# plt.subplot(2, 1, 1)
# plt.bar(departments, salaries, color="black", width=0.5)
# plt.title("Salaries per department")
# plt.xlabel("Departments")
# plt.ylabel("Salaries")

# plt.subplot(2, 1, 2)
# plt.pie(salaries, labels=departments, explode=[0, 0, 0.1, 0], autopct="%1.1f%%")

# plt.tight_layout()
# plt.show()


#Task 11.
# Pandas grouping
# import pandas as pd
# import sqlite3

# with sqlite3.connect("company.db") as connection:
#     df = pd.read_sql("SELECT * FROM employees", con= connection)
#     grouped_df = df.groupby(by="department")

#     df["salary_after_tax"] = df["salary"] * 0.7
#     df.to_parquet("employees.parquet")

#     print(grouped_df["salary"].agg(["sum", "mean"]))




























