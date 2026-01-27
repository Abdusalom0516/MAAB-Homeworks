# ### Task 1

# | Name           | Rank       |
# |----------------|------------|
# | Benjamin Sisko | Captain    |
# | Ezri Dax       | Lieutenant |
# | Kira Nerys     | Major      |

import sqlite3

with sqlite3.connect("roster.db") as connect:
    cursor = connect.cursor()

    drop_table_query = "DROP TABLE IF EXISTS Roster"
    cursor.execute(drop_table_query)

    create_table_query = "CREATE TABLE Roster(Name TEXT, Species TEXT, Age int)"
    cursor.execute(create_table_query)

    columns_with_question_mark = ", ".join(["?"] * 3)

    insert_table_query = f"INSERT INTO Roster VALUES ({columns_with_question_mark})"
    cursor.executemany(insert_table_query,[("Benjamin Sisko", "Human", 40), ("Jadzia Dax", "Trill", 300), ("Kira Nerys", "Bajoran", 39) ])

    update_name_query  = "UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'"
    cursor.execute(update_name_query)

    display_name_and_age_query = "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'"
    data = cursor.execute(display_name_and_age_query).fetchall()
    print(data)

    delete_age_over100_query = "DELETE FROM Roster WHERE Age > 100"
    cursor.execute(delete_age_over100_query)

    alter_table_query = "ALTER TABLE Roster ADD COLUMN Rank TEXT"
    cursor.execute(alter_table_query)

    update_rank_values_query ="""
        UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko';
        UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax';
        UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys';
    """
    cursor.executescript(update_rank_values_query)

    sorted_order_query = "SELECT * FROM ROSTER ORDER BY Age DESC"
    data = cursor.execute(sorted_order_query).fetchall()

    print(data)






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