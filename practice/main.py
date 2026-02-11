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
import requests
import csv

BASE_URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(BASE_URL)

if response.status_code == 200:
    response = response.json()
    user_data = []
    for user_info in response:
        name = user_info["name"]
        email = user_info["email"]
        city = user_info["address"]["city"]
        user_data.append({"name": name, "email": email, "city": city})

    with open("user_data.csv", "w") as f:
        writer = csv.DictWriter(f=f, delimiter=",", fieldnames=["name", "email", "city"])
        writer.writeheader()
        writer.writerows(user_data)

    print(user_data)
else:
    print(f"Failed to get! {response.status_code}.")








