import pandas as pd
import numpy as np
import sqlite3

# Task 1.

# Reading csv file using pandas
df = pd.read_csv("super_dirty_students.csv")

# Top 10 values
print(df.head(10))
print("-"*50)

df_columns = df.columns
df_data_per_column = df.count()
missing_values_count_per_column = df.isna().sum()
df_columns = df.columns

# Column Names
print(df_columns)
print("-"*50)

# Data Count Per Columns
print(df_data_per_column)
print("-"*50)

# Misson Values Count Per Column
print(missing_values_count_per_column)
print("-"*50)
