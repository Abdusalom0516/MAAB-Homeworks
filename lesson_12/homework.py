# ### Task 1

# 2. **Insert Data**:
#    - Populate the **Roster** table with the following entries:

# | Name           | Species  | Age |
# |----------------|----------|-----|
# | Benjamin Sisko | Human    | 40  |
# | Jadzia Dax     | Trill    | 300 |
# | Kira Nerys     | Bajoran  | 29  |

# 3. **Update Data**:
#    - Update the `Name` of **Jadzia Dax** to **Ezri Dax**.

# 4. **Query Data**:
#    - Retrieve and display the **Name** and **Age** of all characters where the `Species` is **Bajoran**.

# 5. **Delete Data**:
#    - Remove all characters aged over 100 years from the table.

# 6. **Bonus Task**:
#    - Add a new column called `Rank` to the **Roster** table and update the data with the following values:

# | Name           | Rank       |
# |----------------|------------|
# | Benjamin Sisko | Captain    |
# | Ezri Dax       | Lieutenant |
# | Kira Nerys     | Major      |

# 7. **Advanced Query**:
#    - Retrieve all characters sorted by their `Age` in descending order.
import sqlite3

with sqlite3.connect("roster.db") as connect:
    cursor = connect.cursor()

    create_table_query = "CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, Age int)"
    cursor.execute(create_table_query)

    columns_with_question_mark = ", ".join(["?"] * 3)

    insert_table_query = f"INSERT INTO Roster VALUES ({columns_with_question_mark})"
    cursor.executemany(insert_table_query,[("Benjamin Sisko", "Human", 40), ("Jadzia Dax", "Trill", 300), ("Kira Nerys", "Bajoran", 39) ])






# ### Task 2

# 1. **Database Creation**:
#    - Create a new SQLite database named `library.db`.
#    - Define a table called **Books** with the following schema:
#      - **Title**: TEXT
#      - **Author**: TEXT
#      - **Year_Published**: INTEGER
#      - **Genre**: TEXT

# 2. **Insert Data**:
#    - Populate the **Books** table with the following entries:

# | Title                  | Author          | Year_Published | Genre      |
# |------------------------|-----------------|----------------|------------|
# | To Kill a Mockingbird  | Harper Lee      | 1960           | Fiction    |
# | 1984                   | George Orwell   | 1949           | Dystopian  |
# | The Great Gatsby       | F. Scott Fitzgerald | 1925        | Classic    |

# 3. **Update Data**:
#    - Update the `Year_Published` of **1984** to **1950**.

# 4. **Query Data**:
#    - Retrieve and display the **Title** and **Author** of all books where the `Genre` is **Dystopian**.

# 5. **Delete Data**:
#    - Remove all books published before the year 1950 from the table.

# 6. **Bonus Task**:
#    - Add a new column called `Rating` to the **Books** table and update the data with the following values:

# | Title                  | Rating |
# |------------------------|--------|
# | To Kill a Mockingbird  | 4.8    |
# | 1984                   | 4.7    |
# | The Great Gatsby       | 4.5    |

# 7. **Advanced Query**:
#    - Retrieve all books sorted by their `Year_Published` in ascending order.

# ---