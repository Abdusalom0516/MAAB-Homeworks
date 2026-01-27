# ### Task 1

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

with sqlite3.connect("library.db") as connect:
    cursor = connect.cursor()

    delete_table_query = "DROP TABLE IF EXISTS Books"
    cursor.execute(delete_table_query)

    create_table_query = "CREATE TABLE Books(Title TEXT, Author TEXT, Year_Published int, Genre TEXT)"
    cursor.execute(create_table_query)

    columns_with_question_mark = ", ".join(["?"] * 4)
    insert_values_query = f"INSERT INTO Books Values({columns_with_question_mark})"
    cursor.executemany(insert_values_query, [("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"), ("1984", "George Orwell", 1949, "Dystopian"), ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")])

    update_year_query = "UPDATE Books SET Year_Published = 1950 WHERE Title = 1984"
    cursor.execute(update_year_query)

    filter_by_genre_query = "SELECT* FROM Books WHERE Genre = 'Dystopian'"
    data = cursor.execute(filter_by_genre_query).fetchall()
    print(data)

    delete_books_query = "DELETE FROM Books WHERE Year_Published < 1950"
    cursor.execute(delete_books_query)

    alter_table_query = "ALTER TABLE Books ADD COLUMN Rating DECIMAL"
    cursor.execute(alter_table_query)

    update_rating_values_query = """
        UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird';
        UPDATE Books SET Rating = 4.7 WHERE Title = '1984';
        UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby';
    """
    cursor.executescript(update_rating_values_query)

    sorted_by_year_query = "SELECT * FROM Books ORDER BY Year_Published"
    data = cursor.execute(sorted_by_year_query).fetchall()
    print(data)





