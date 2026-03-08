import json
import csv

with open("data.json", "r") as f:
    data = json.load(f)

    print(dict(data[0]).keys)


with open("data.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=dict(data[0]).keys())

    writer.writeheader()
    writer.writerows(data)


import pandas as pd

df = pd.read_json("data.json")

df.to_excel("task2.xlsx",sheet_name="task1")
# print(df)



import pandas as pd

df = pd.read_json("data.json")

df["last_name"] = df["last_name"].str.strip()

def gender_return(last_name):
    if last_name[len(last_name)-1] == "a":
        return "F"
    else:
        return "M"

df["gender"] = df["last_name"].apply(gender_return)


active_users = df[df["is_active"] == True]
inactive_users = df[df["is_active"] == False]

inactive_users.to_csv("inactive_users.csv")
active_users.to_csv("active_users.csv")

print(df)

print("-----------------")


import pandas as pd

df = pd.read_json("data.json")

grouped_df = df.groupby(by="department")

df = grouped_df.agg({
    "salary": ["mean", "max", "min", "std"],
    "employee_id": ["count"]
})

df.columns = ["mean", "max", "min", "std", "NoEmp"]
df.to_excel("last_task.xlsx", sheet_name="last_task")

print(df)



