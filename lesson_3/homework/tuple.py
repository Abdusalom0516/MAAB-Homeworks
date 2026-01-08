# Task 1
print("--------- TASK 1 -----------")
myTuple = ("Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime")
element = "freedom"

occurrencesCount = myTuple.count(element)

print(myTuple)
print(element)
print(occurrencesCount)



# Task 2
print("--------- TASK 2 -----------")
myTuple = (-2, 54, -90, 32, 77, 120)

maxElem = -99999999999999999

for elem in myTuple:
    if elem > maxElem:
        maxElem = elem

print(myTuple)
print(maxElem)



# Task 3
print("--------- TASK 3 -----------")
myTuple = (-2, 54, -90, 32, 77, 120)

minElem = 99999999999999999

for elem in myTuple:
    if elem < minElem:
        minElem = elem

print(myTuple)
print(minElem)



# Task 4
print("--------- TASK 4 -----------")
myTuple = ("Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime")
element = "freedom"

if myTuple.count(element) > 0:
    print(True)
else:
    print(False)



# Task 5
print("--------- TASK 5 -----------")
myTuple = ("Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime")

firstElement = "Empty"

if myTuple:
    firstElement = myTuple[0]

print(myTuple)
print(firstElement)



# Task 6
print("--------- TASK 6 -----------")
myTuple = ("Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime")

lastElement = "Empty"

if myTuple:
    firstElement = myTuple[len(myTuple)-1]

print(myTuple)
print(firstElement)



# Task 7
print("--------- TASK 7 -----------")
myTuple = ("Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime")

length = len(myTuple)

print(myTuple)
print(length)



# Task 8
print("--------- TASK 8 -----------")
myTuple = ("Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime")

sliceTuple = myTuple[0:3]

print(myTuple)
print(sliceTuple)


# Task 9
print("--------- TASK 9 -----------")
myTuple = ("Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime")
myTuple2 = ("Naruto", "Steel Ball Run", "Avatar", "Supernatural")

concatenatedTuple = tuple((*myTuple, *myTuple2))

print(myTuple)
print(myTuple2)
print(concatenatedTuple)



# Task 10
print("--------- TASK 10 -----------")
myTuple = ("Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime")

if myTuple:
    print("Given tuple is not empty.")
else:
     print("Given tuple is empty.")