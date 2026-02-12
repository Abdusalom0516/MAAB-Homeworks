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


# Task 11.
# Pandas grouping
# import pandas as pd
# import sqlite3

# with sqlite3.connect("company.db") as connection:
#     df = pd.read_sql("SELECT * FROM employees", con= connection)
#     grouped_df = df.groupby(by="department")

#     df["salary_after_tax"] = df["salary"] * 0.7
#     df.to_parquet("employees.parquet")

#     print(grouped_df["salary"].agg(["sum", "mean"]))



# Task 12.
import pandas as pd

# -----------------------------
# Customers Table
# -----------------------------
customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5, 6],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "city": ["New York", "London", "New York", "Paris", "Berlin", "Tokyo"],
    "signup_date": pd.to_datetime([
        "2023-01-10", "2023-03-22", "2023-04-05",
        "2023-06-18", "2023-07-30", "2023-09-12"
    ])
})

# -----------------------------
# Orders Table
# -----------------------------
orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "customer_id": [1, 2, 1, 3, 7, 2, 4, 1],  # customer_id=7 does NOT exist (join challenge)
    "order_date": pd.to_datetime([
        "2024-01-02", "2024-01-05", "2024-01-20", "2024-02-11",
        "2024-02-15", "2024-03-01", "2024-03-03", "2024-03-10"
    ]),
    "total_amount": [120, 80, 250, 60, 90, 300, 150, 200]
})

# -----------------------------
# Products Table
# -----------------------------
products = pd.DataFrame({
    "product_id": [11, 12, 13, 14, 15],
    "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "category": ["Electronics", "Electronics", "Electronics", "Electronics", "Accessories"],
    "price": [1000, 25, 75, 300, 150]
})

# -----------------------------
# Order Items (Bridge Table)
# -----------------------------
order_items = pd.DataFrame({
    "order_id": [101, 101, 102, 103, 104, 105, 106, 106, 107, 108],
    "product_id": [11, 12, 12, 13, 15, 14, 11, 15, 13, 12],
    "quantity": [1, 2, 3, 1, 1, 1, 1, 2, 2, 4]
})

# -----------------------------
# Payments Table
# -----------------------------
payments = pd.DataFrame({
    "payment_id": [5001, 5002, 5003, 5004, 5005, 5006],
    "order_id": [101, 102, 103, 104, 106, 110],  # 110 does not exist
    "payment_method": ["Card", "PayPal", "Card", "Card", "Wire", "Card"],
    "payment_status": ["Completed", "Completed", "Refunded", "Completed", "Completed", "Failed"]
})

# -----------------------------
# Reviews Table
# -----------------------------
reviews = pd.DataFrame({
    "review_id": [9001, 9002, 9003, 9004, 9005],
    "product_id": [11, 12, 11, 15, 99],  # 99 missing product
    "rating": [5, 4, 3, 5, 2]
})


joined = orders.join(customers, on="customer_id",  lsuffix=None, rsuffix="_other", how="inner")[["customer_id", "name", "order_id", "order_date", "total_amount"]]
print(joined)


def my_function(df):
    return df[df["total_amount"] > 100]

df = joined.pipe(my_function)
print(df)


























