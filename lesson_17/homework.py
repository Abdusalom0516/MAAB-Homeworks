import numpy as np
import pandas as pd
import sqlite3


# #### **Merging and Joining**
# 1. **Inner Join on Chinook Database**
#    - Load the `chinook.db` database.
#    - Perform an inner join between the `customers` and `invoices` tables on the `CustomerId` column.
#    - Find the total number of invoices for each customer.

with sqlite3.connect("chinook.db") as connection:
    customers_df = pd.read_sql_query("SELECT * FROM customers", con=connection)
    invoices_df = pd.read_sql_query("SELECT* FROM Invoices", con=connection)

    joined_df = pd.merge(left=customers_df, right=invoices_df, on="CustomerId", how="inner", suffixes=[None, "_other"])
    grouped_df = joined_df.groupby(by="CustomerId")
    print(grouped_df["InvoiceId"].count().reset_index())



# 2. **Outer Join on Movie Data**
#    - Load the `movie.csv` file.
#    - Create two smaller DataFrames:
#      - One with only `director_name` and `color`.
#      - Another with `director_name` and `num_critic_for_reviews`.
#    - Perform a left join and then a full outer join on `director_name`.
#    - Count how many rows are in the resulting DataFrames for each join type.
# ---

df_csv = pd.read_csv("movie.csv")

df_1 = df_csv[["director_name", "color"]]
df_2 = df_csv[["director_name", "num_critic_for_reviews"]]

left_joined = pd.merge(df_1, df_2, on="director_name", how="left", suffixes=["_left", "_right"])
outer_joined = pd.merge(df_1, df_2, on="director_name", how="outer", suffixes=["_left", "_right"])

number_of_rows_in_left_joined = len(left_joined)
number_of_rows_in_outer_joined = len(outer_joined)
print("Left Joined rows count:", number_of_rows_in_left_joined)
print("Outer Joined rows count:", number_of_rows_in_outer_joined)


# #### **Grouping and Aggregating**

# 1. **Grouped Aggregations on Titanic**
#    - Group passengers by `Pclass` and calculate the following:
#      - Average age.
#      - Total fare.
#      - Count of passengers.
#    - Save the results to a new DataFrame.

df_excel = pd.read_excel("titanic.xlsx")
print(df_excel)

grouped_df = df_excel.groupby(by="Pclass")

result = grouped_df.agg({
    "Age": ["mean"],
    "Fare": ["sum"],
    "PassengerId": ["count"]
}).reset_index()

result.columns = ["Pclass","Average age", "Total fare", "Passengers count"]
print(result)

#  2. **Multi-level Grouping on Movie Data**
#    - Group the movies by `color` and `director_name`.
#    - Find:
#      - Total `num_critic_for_reviews` for each group.
#      - Average `duration` for each group.

df_excel = pd.read_csv("movie.csv")
grouped_df = df_excel.groupby(["color", "director_name"])

result = grouped_df.agg({
    "num_critic_for_reviews": ["sum"],
    "duration": ["mean"]
}).reset_index()

level0_column_names = result.columns.get_level_values(0)
level1_column_names = result.columns.get_level_values(1)

new_column = [str(level0+"_"+level1).removesuffix("_") for level0, level1 in zip(level0_column_names, level1_column_names)]
result.columns = new_column
print(result)





# #### **Using `pipe`**
# 1. **Pipeline on Titanic**
#    - Create a pipeline to:
#      - Filter passengers who survived (`Survived == 1`).
#      - Fill missing `Age` values with the mean.
#      - Create a new column, `Fare_Per_Age`, by dividing `Fare` by `Age`.

df = pd.read_excel("titanic.xlsx")
survived_passangers_df = df[df["Survived"] == 1]
survived_passangers_df["Age"] = survived_passangers_df["Age"].fillna(survived_passangers_df["Age"].mean())
survived_passangers_df["Fare_Per_Age"] = survived_passangers_df["Fare"] / survived_passangers_df["Age"]
print(survived_passangers_df)










