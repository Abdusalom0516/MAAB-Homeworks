# Task 1.
data = ["5", "12", "hello", "34", "", "18", "NaN", "50"]
valid_numbers = []

for elem in data:
    try:
        valid_numbers.append(int(elem))
    except:
        pass

print(valid_numbers)


# Task 2.
class Student:
    def __init__(self, *, name: str, grade: int):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student(name={self.name}, grade={self.grade}.)"

    def increase_grade(self, percent: float):
        self.grade = round(self.grade + (self.grade / 100) * percent)
        if self.grade > 100:
            self.grade = 100

    def display_info(self):
        print(f"Student name: {self.name}, student grade: {self.grade}.")

student = Student(name="Abdusalom", grade=50)
student.display_info()
student.increase_grade(10)
student.display_info()


# Task 3.
import numpy as np

arr = np.array([5, 22, 13, 45, 8, 31, 60, 2])

greater_than_25 = arr[arr > 25]
print(greater_than_25)

between_10_and_40 = arr[(arr >= 10) & (arr <= 40)]
print(between_10_and_40)

even_numbers = arr[arr % 2 == 0]
print(even_numbers)

square_numbers = arr ** 2
print(square_numbers)


# Task 4.
import numpy as np

matrix = np.random.randint(1, 11, (3, 3))
print(matrix)

col_mean = matrix.mean(axis=0)
row_mean = matrix.mean(axis=1)
min_value = matrix.min()
max_value = matrix.max()
transpose_matrix = matrix.transpose()
flattened = matrix.flatten()

print("--------")
print(transpose_matrix)
print(flattened)
print("--------")
print(col_mean)
print(row_mean)
print(min_value)
print(max_value)


# Task 5.
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(URL)

if response.status_code == 200:
    print("Success")
    response = response.json()
    print(response[0])

    posts_list = []
    for elem in response:
        posts_list.append({
            "userId": elem["userId"],
            "id": elem["id"],
            "title": elem["title"]
        })

    with open("posts.csv", "w") as f:
        writer = csv.DictWriter(f=f, fieldnames=["userId", "id", "title"])
        writer.writeheader()
        writer.writerows(posts_list)
else:
    print("Failure")


# Task 6.
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com"

response = requests.get(URL)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []

    all_quotes = soup.find_all("div", class_="quote")

    for elem in all_quotes:
        text = elem.find("span", class_="text")
        author = elem.find("span", class_="author")
        quotes.append([{
            "quote": text,
            "author": author
        }])

    print(quotes)

else:
    print(f"Failure {response.status_code}, {response.reason}.")


# Task 7.
import sqlite3
import pandas as pd

with sqlite3.connect("school.db") as connection:
    cursor = connection.cursor()
    query = """
        drop table if exists students;
        create table students(
            id INTEGER,
            name TEXT,
            age INTEGER,
            grade TEXT
        )
    """
    cursor.executescript(query)

    cursor.executescript(
        """
            insert into students
            values
            (1, "Ali", 17, "A"),
            (2, "Vali", 19, "B"),
            (3, "Sara", 21, "A"),
            (4, "John", 18, "C"),
            (5, "Lola", 22, "B")
        """
    )

    df = pd.read_sql("SELECT * FROM students WHERE age > 18", con=connection)
    print(df)


