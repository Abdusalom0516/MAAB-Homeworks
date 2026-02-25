# ----- Python Final Exam -----

# task 1
# ----------------------------------------------------------------------------------------------------
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

# Misollar:
# Kiritish:
# 24
# Natija:
# 6
# (Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)

# Kiritish:
# 502
# Natija:
# 7
# (Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)
# ----------------------------------------------------------------------------------------------------
print("-"*20 + "Task 1" + "-"*20)
def digit_sum(number) -> int:
    converted = str(number)
    number_sum = 0

    for elem in converted:
        number_sum += int(elem)

    return number_sum

print(digit_sum(123456))



# task 2
# -----------------------------------------------------------------------------------------------------
#  Define a function `is_prime(n)` which returns `True` if the given n (n > 0) is prime number, otherwise returns `False`.
print("-"*20 + "Task 2" + "-"*20)
def is_prime(n) -> bool:
    divisable_count = 0
    for elem in range(n):
        if n % (elem+1) == 0:
            divisable_count += 1

        if divisable_count > 2:
            return False

    return True

print(is_prime(11))
print(is_prime(12))
print(is_prime(3))

# ----------------------------------------------------------------------------------------------------

# task 3
# ----------------------------------------------------------------------------------------------------
# 1) Create a new database with a table named Roster that has three fields: Name, Species, and Age.
# The Name and Species columns should be text fields, and the Age column should be an integer field.


# 2)  Populate your new table with the following values:

# | Name            | Species      | Age |
# |-----------------|--------------|-----|
# | Benjamin Sisko  | Human        |  40 |
# | Jadzia Dax      | Trill        | 300 |
# | Kira Nerys      | Bajoran      |  29 |


# 3)  Display the Name and Age of everyone in the table classified as Bajoran.

import sqlite3
import pandas as pd

print("-"*20 + "Task 3" + "-"*20)

with sqlite3.connect("roster.db") as connection:
    cursor = connection.cursor()

    create_table_query = """
        DROP TABLE IF EXISTS Roster;
        CREATE TABLE Roster
        (
            Name text,
            Species text,
            Age int
        )
    """

    cursor.executescript(create_table_query)

    insert_value_query = """
        INSERT INTO Roster
        VALUES
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Troll', 300),
        ('Kira Nerys', 'Bajoran', 29)
    """

    cursor.executescript(insert_value_query)

    all_bajorans_query = """
        SELECT * FROM Roster
        WHERE Species = 'Bajoran'
    """
    all_bajorans_name_and_age = pd.read_sql_query(all_bajorans_query, con=connection)[["Name", "Age"]]
    print(all_bajorans_name_and_age)






# task 4
# -----------------------------------------------------------------------------------------------------
# Update employees.json file by adding new worker's info. (Use Input command to get info)
print("-"*20 + "Task 4" + "-"*20)

# import pandas as pd
import json

# df_employees = pd.read_json("employees.json")["employees"]
# df_employees = df_employees.reset_index()


# print(df_employees["employees"])

new_employeeID = int(input("Enter new employeeID: "))
new_employee_name = input("Enter new employee name: ")
new_employee_role = input("Enter new employee role: ")
new_employee_department = input("Enter new empoyee department: ")
new_employee_salary = int(input("Enter new employee salary: "))

all_employees = []
with open("employees.json", "r") as f:
    all_employees = json.load(f)["employees"]
    print(all_employees)

with open("employees.json", "w") as f:
    new_employee_data = {
        'id': new_employeeID,
        'name': new_employee_name,
        'role': new_employee_role,
        'department': new_employee_department,
        'salary': new_employee_salary
    }
    all_employees.append(new_employee_data)
    print(all_employees)


    json.dump({"employees": all_employees}, f, indent=4)








# task 5
# -----------------------------------------------------------------------------------------------------
# You have a dataset (customer_orders.csv) containing information about customer orders. The dataset has the following columns:

# OrderID: Unique identifier for each order.
# CustomerID: Unique identifier for each customer.
# Product: Name of the product ordered.
# Quantity: Number of units ordered.
# Price: Price per unit.
# Tasks:

# 1)Group the data by CustomerID and filter out customers who have made less than 20 orders.
# 2)Identify customers who have ordered products with an average price per unit greater than $120.

import pandas as pd

print("-"*20 + "Task 5" + "-"*20)

# 1) Group the data by CustomerID and filter out customers who have made less than 20 orders.
df = pd.read_csv("customer_orders.csv")

grouped_by_cus_id = df.groupby(by="CustomerID")

customers_order_count = grouped_by_cus_id["OrderID"].count()

customers_order_count = customers_order_count.reset_index()

customers_order_count.columns = ["CustomerID", "OrderCount"]

customers_with_less_than_20_orders = customers_order_count[customers_order_count["OrderCount"] < 20]

print(customers_with_less_than_20_orders)


# 2) Identify customers who have ordered products with an average price per unit greater than $120.
df = pd.read_csv("customer_orders.csv")

grouped_by_cus_id = df.groupby(by="CustomerID")

customers_with_product_avg = grouped_by_cus_id["Price"].mean()
customers_with_product_avg = customers_with_product_avg.reset_index()

customers_with_product_avg.columns = ["CustomerID", "OrderedProdAvg"]

customers_ordered_prod_avg_greater_than_120_dollar = customers_with_product_avg[customers_with_product_avg["OrderedProdAvg"] > 120]

print(customers_ordered_prod_avg_greater_than_120_dollar)





