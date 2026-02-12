import sqlite3

connection = sqlite3.connect("test.db")

query = "select datetime('now', 'localtime')"

cursor = connection.cursor()
time = cursor.execute(query)

print(time.fetchone())
print(time.fetchmany())
print(time.fetchall())

connection.close()


with sqlite3.connect("test.db") as connect:
    query = "select datetime('now', 'localtime')"

    cursor = connect.cursor()
    time = cursor.execute(query)

    print(time.fetchone())
    print(time.fetchmany())
    print(time.fetchall())


with sqlite3.connect("animes.db") as connect:
    cursor = connect.cursor()
    query = "CREATE TABLE IF NOT EXISTS animes(id int, name text)"
    cursor.execute(query)
    cursor.executemany(
        "INSERT INTO animes VALUES(?, ?)", # Runs this 3 times because we have 3 values and adds the values to the '?' places.
        [(1, 'Vinland Saga'),
         (2, 'Hunter X Hunter'),
         (3, "Jojo's Bizzare Adventure")
        ]
    )

placeholder = ", ".join(["1", "2", "3", "4", "5"] * 3)
print(placeholder)



