# from collections import Counter

# genders = ["Male", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Female"]
# print(Counter(genders))


# import pandas as pd

# df = pd.read_csv("employee.csv")
# print(type(df))
# print(df)

# df = pd.read_json("employee.json")
# print(df)


# import sqlite3

# with sqlite3.connect("chinook.db") as connection:
#     df = pd.read_sql(
#         "SELECT * FROM employees",
#         con=connection
#     )

#     print(df)


# from sqlalchemy import create_engine


# from getpass import getpass

# password = getpass() # Invisable Input


# columns = ["Title", "Score", "Year", ]
# data = [
#     ["Saw 5", 7.5, 2012],
#     ["Avatar 3", 8.9, 2025],
# ]


# df = pd.DataFrame(data=data, columns=columns)
# print(df)

# print(df.info())

# titles = df[["Title", "Year"]]
# print(titles)


# budgets = [4000000, 5000000]


# df["budget"] = ["low" if elem <= 4000000 else "high" for elem in budgets]
# print(df)

# import numpy as np

# budgets = np.array([4000000, 5000000])

# new_array = np.where(budgets <= 4000000, "low", "high")
# print(new_array)

# df["costs"] = new_array

# df.drop(columns=["costs"], inplace=True)

# # df.drop(1,axis=0, inplace=True) # if axis is 0 then removes from rows if it is 1 then it removes from columns.

# print(df)

# print(df[df["Title"] == "Saw 5"])

# print(df["Score"].sort_values(ascending=True))

# df["Score"].sort_values(ascending=True)

# print(df.sort_values(by="Year", ascending=False))

# print(df["budget"].isnull())

# df = pd.DataFrame(columns=["name", "age", "salary"], data=[["Abdusalom", 20, 2500], ["Abdulmalik", None, 4000], ["Jasur", 23, 3000]])


# # print(df.dropna(subset="salary")) # Drops rows with NaN values. if subset is spesified then it checks only that columns values.

# df.fillna(inplace=True, value=0)
# print(df)


import pandas as pd

data = ["Malika", "Munisa", "Fotima"]
series = pd.Series(data, index=["1", "2", "3"])

print(series.loc["1"])


data = {
    "names": ["Malika", "Munisa", "Fotima"],
    "roles": ["Daughter", "Daughter", "Wife"]
}

df = pd.DataFrame(data, index=["Member 1", "Member 2", "Member 3"])

print(df)


new_data = {
    "names": ["Muhammad", "Abdusalom", "Abdulmalik"],
    "roles": ["Son", "Husband", "Son"]
}

new_df = pd.DataFrame(new_data, index=["Member 4", "Member 5", "Member 6"])

df = pd.concat([df, new_df])
print(df)

print(df.loc["Member 5"].values)

##### AGGREGATION #######

grouped_df = df.groupby("roles")
print(grouped_df.count())

df = pd.DataFrame(df["roles"].replace(to_replace="Wife", value="Wife/Mother"))
print(df)

df = pd.DataFrame(df["roles"].replace(to_replace="Husband", value="Husband/Father"))
print(df)

df.to_parquet("data.parquet")



