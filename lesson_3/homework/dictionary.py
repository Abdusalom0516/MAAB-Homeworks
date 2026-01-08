# Task 1
print("--------- TASK 1 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}
key = "title"

print(key)
if key in dictionary:
    print(dictionary[key])
else:
    print("Key not found.")


# Task 2
print("--------- TASK 2 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}
key = "genre"

print(key)
if key in dictionary:
    print("Key exists.")
else:
    print("Key not found.")


# Task 3
print("--------- TASK 3 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}

countKeys = len(dictionary)

print(f"There is/are {countKeys} keys in the {dictionary}.")