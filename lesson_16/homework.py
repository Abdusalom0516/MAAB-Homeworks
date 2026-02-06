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



