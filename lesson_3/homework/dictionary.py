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


# Task 4
print("--------- TASK 4 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}

keysList = []
for elem in dictionary.keys():
    keysList.append(elem)

print(keysList)


# Task 5
print("--------- TASK 5 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}

valuesList = []
for elem in dictionary.values():
    valuesList.append(elem)

print(valuesList)


# Task 6
print("--------- TASK 6 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}

dictionary2 = {
  'year': '2026',
  'mainHero': 'Toji',
  'director': 'Takashi Hushiguro',
}

newDict = {}
newDict.update(dictionary)
newDict.update(dictionary2)

print(newDict)


# Task 7
print("--------- TASK 7 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}

key = "ongoing"

print(dictionary)
print(key)
removedValue = dictionary.pop(key, "Key not found!")

print(dictionary)


# Task 8
print("--------- TASK 8 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}

print(dictionary)
dictionary.clear()
print(dictionary)


# Task 9
print("--------- TASK 9 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}

if dictionary:
    print("Given dictionary is not empty.")
else:
    print("Given dictionary is empty.")


# Task 10
print("--------- TASK 10 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}
key = "title"

if key in dictionary:
    print({key: dictionary[key]})
else:
    print("Key not found!")


# Task 11
print("--------- TASK 11 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False
}
key = "title"
newValue = "Vinland Saga"

print(dictionary)
dictionary.update({key: newValue})
print(dictionary)


# Task 12
print("--------- TASK 12 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False,
  'ongoingEpisodes': 24
}

value = 24
countValueOccurences = 0

for elem in dictionary.values():
    if value == elem:
        countValueOccurences+=1

print(dictionary)
print(value)
print(countValueOccurences)


# Task 13
print("--------- TASK 13 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False,
  'ongoingEpisodes': 24
}

newDict = {}

for elem in dictionary.items():
    newDict.update({elem[1]: elem[0]})

print(dictionary)
print(newDict)


# Task 14
print("--------- TASK 14 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False,
  'ongoingEpisodes': 24
}
value = 24

listOfKeys = []

for elem in dictionary.items():
    if elem[1] == value:
        listOfKeys.append(elem[0])

print(dictionary)
print(value)
print(listOfKeys)


# Task 15
print("--------- TASK 15 -----------")
keysList = ["name", "age", "userame"]
valuesList = ["Abdusalom", 20, "freedom"]

dictionary = {}

for i in range(len(keysList)):
    dictionary.update({keysList[i]: valuesList[i]})

print(keysList)
print(valuesList)
print(dictionary)


# Task 16
print("--------- TASK 16 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False,
  'ongoingEpisodes': {}
}

isNestedDict = False
for elem in dictionary.values():
    if type(elem) is type(dict()):
        isNestedDict = True
        break

if isNestedDict:
    print("Given dictionary contains another dictionary.")
else:
    print("Given dictionary doesn't contain another dictionary.")


# Task 17
print("--------- TASK 17 -----------")
dictionary = {
  'title': {'name': 'Jujutsu Kaisen', 'year': 2026},
  'genre': {'name': 'Drama', 'popularity': 95},
}

print(dictionary)
for elem in dictionary.values():
    for innerElem in elem.values():
        print(innerElem)


# Task 18
print("--------- TASK 18 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False,
  'ongoingEpisodes': {}
}
key = "anime"

print(dictionary.get(key, f"{key} key not found!"))


# Task 19
print("--------- TASK 19 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False,
  'best': 24
}

uniqueNumbersCount = 0
myList = []
for elem in dictionary.values():
    myList.append(elem)


uniqueNumbersCount = len(set(myList))

print(dictionary)
print(uniqueNumbersCount)


# Task 20
print("--------- TASK 20 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False,
  'ongoingEpisodes': {}
}

sortedByKey = dict(sorted(dictionary.copy().items(), key=lambda item: item[0]))

print(dictionary)
print(sortedByKey)


# Task 21
print("--------- TASK 21 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'ABBA',
}

sortedByValue = dict(sorted(dictionary.copy().items(), key=lambda item: item[1]))

print(dictionary)
print(sortedByValue)


# Task 22
print("--------- TASK 22 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False,
  'ongoingEpisodes': {}
}

newDictionary = {}
for item in dictionary.items():
    if type(item[1]) is str:
        newDictionary.update({item[0]: item[1]})

print(newDictionary)


# Task 23
print("--------- TASK 23 -----------")
dictionary1 = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
}

dictionary2 = {
  'age': 20,
  'genre': 'Supernatural',
  'name': 'Abdusalom',
}

commonKeys = set()
for key in dictionary1.keys():
    if key in dictionary2:
        commonKeys.add(key)

for key in dictionary2.keys():
    if key in dictionary1:
        commonKeys.add(key)

commonKeys = list(commonKeys)

print(dictionary1)
print(dictionary2)
print(commonKeys)


# Task 24
print("--------- TASK 24 -----------")
myTuple = ("age", 20)

dictionary = {myTuple[0]: myTuple[1]}

print(myTuple)
print(dictionary)


# Task 25
print("--------- TASK 25 -----------")
dictionary = {
  'title': 'Jujutsu Kaisen',
  'genre': 'Supernatural',
  'studio': 'MAPPA',
  'episodes': 24,
  'rating': 8.9,
  'ongoing': False,
  'ongoingEpisodes': {}
}

firstKeyValue = {}
for elem in dictionary.items():
    if not firstKeyValue:
        firstKeyValue = {elem[0]: elem[1]}
        break
        

print(firstKeyValue)

