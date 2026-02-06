import numpy as np
import pandas as pd
import sqlite3
import csv

#### Part 1: Reading Files

# 1.
with sqlite3.connect("chinook.db") as connetion:
    df = pd.read_sql_query("SELECT * FROM customers", connetion)
    print(df.head(10))




