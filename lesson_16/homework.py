import numpy as np
import pandas as pd
import sqlite3

#### Part 1: Reading Files

# # 1.
# with sqlite3.connect("chinook.db") as connection:
#     df = pd.read_sql_query("SELECT * FROM customers", connection)
#     print(df.head(10))


# # 2. **`iris.json`**
# #    - Load the JSON file into a DataFrame. Show the shape of the dataset and the column names.

# df_json = pd.read_json("iris.json")
# column_names = df_json.columns
# print(df.shape)
# print(column_names)


# # 3. **`titanic.xlsx`**  
# #    - Load the Excel file into a DataFrame. Use `head` to display the first 5 rows.

# df_excel = pd.read_excel("titanic.xlsx")
# print(df_excel.head(5))


# 4. **Flights parquet file**
#    - Read the Parquet file into a DataFrame and use `info` to summarize it.

# df_parquet = pd.read_parquet("flights.parquet")
# print(df_parquet.info())


# 5. **`movie.csv`**
#    - Load the CSV file into a DataFrame and display a random sample of 10 rows.

# df_csv = pd.read_csv("movie.csv")
# print(df_csv.sample(10))



# #### Part 2: Exploring DataFrames  
# 1. Using the DataFrame from **`iris.json`**:  
#    - Rename the columns to lowercase.  
#    - Select only the `sepal_length` and `sepal_width` columns.  

# df_json = pd.read_json('iris.json')
# df_json.columns = [elem.lower() for elem in df_json.columns] # First approach
# df_json.columns = df_json.columns.str.lower() # Second approach
# print(df_json[["sepal_length", "sepal_width"]])


# 2. From the **`titanic.xlsx`** DataFrame:  
#    - Filter rows where the age of passengers is above 30.  
#    - Count the number of male and female passengers (`value_counts`).  

# df_excel = pd.read_json("employee.json")
# filteres_df = df_excel[df_excel["age"] > 30]
# group_by_gender = df_excel.groupby("sex")

# print(filteres_df)
# print(group_by_gender["sex"].count())


# 3. From the **Flights parquet file**:
#    - Extract and print only the `origin`, `dest`, and `carrier` columns.  
#    - Find the number of unique destinations.

# df_parquet = pd.read_parquet("flight.parquet")
# number_of_uinque_destinations = len(df_excel.groupby("dest"))
# print(df_parquet[["origin", "dest", "carrier"]])
# print(number_of_uinque_destinations)

# 4. From the **`movie.csv`** file:  
#    - Filter rows where `duration` is greater than 120 minutes.  
#    - Sort the filtered DataFrame by `director_facebook_likes` in descending order.  

# df_csv = pd.read_csv("movie.csv")
# filtered_df = df_csv[df_csv["duration"] > 120]
# print(filtered_df.sort_values(by="director_facebook_likes",ascending=False))






