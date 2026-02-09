import numpy as np
import pandas as pd


# #### **Merging and Joining**
# 1. **Inner Join on Chinook Database**
#    - Load the `chinook.db` database.
#    - Perform an inner join between the `customers` and `invoices` tables on the `CustomerId` column.
#    - Find the total number of invoices for each customer.

# 2. **Outer Join on Movie Data**
#    - Load the `movie.csv` file.
#    - Create two smaller DataFrames:
#      - One with only `director_name` and `color`.
#      - Another with `director_name` and `num_critic_for_reviews`.
#    - Perform a left join and then a full outer join on `director_name`.
#    - Count how many rows are in the resulting DataFrames for each join type.

# ---

# #### **Grouping and Aggregating**
# 1. **Grouped Aggregations on Titanic**
#    - Group passengers by `Pclass` and calculate the following:
#      - Average age.
#      - Total fare.
#      - Count of passengers.
#    - Save the results to a new DataFrame.

# 2. **Multi-level Grouping on Movie Data**
#    - Group the movies by `color` and `director_name`.
#    - Find:
#      - Total `num_critic_for_reviews` for each group.
#      - Average `duration` for each group.

# 3. **Nested Grouping on Flights**
#    - Group flights by `Year` and `Month` and calculate:
#      - Total number of flights.
#      - Average arrival delay (`ArrDelay`).
#      - Maximum departure delay (`DepDelay`).

# ---
