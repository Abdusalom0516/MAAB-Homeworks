# Exceptions

class CustomException(Exception):
    pass

try:
    raise CustomException("Fuck you.")
except CustomException as ce:
    print(ce)

print("-------------------------------")

import csv

with open("tasks.csv", "r") as f:
    tasks = csv.reader(f)

    for elem in tasks:
        print(elem)


# with open("tasks.csv", "w") as f:
#     writer = csv.writer(f)

#     writer.writerow()


from pkg import User

user = User()

