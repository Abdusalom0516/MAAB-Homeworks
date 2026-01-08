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



# Task 11
print("--------- TASK 11 -----------")
myTuple = ("Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime")
element = "freedom"

indices = []

for i in range(len(myTuple)):
    if myTuple[i] == element:
        indices.append(i)

indices = tuple(indices)

print(myTuple)
print(element)
print(indices)


# Task 12
print("--------- TASK 12 -----------")
myTuple = (-2, 54, -90, 32, 77, 120)

myList = list(myTuple)
myList.sort(reverse=True)

secondLargest = myList[1]


print(myTuple)
print(secondLargest)



# Task 13
print("--------- TASK 13 -----------")
myTuple = (-2, 54, -90, 32, 77, 120)

myList = list(myTuple)
myList.sort()

secondSmallest = myList[1]


print(myTuple)
print(secondSmallest)



# Task 14
print("--------- TASK 14 -----------")

singleElementTuple = (999, )

print(type(singleElementTuple))
print(singleElementTuple)



# Task 15
print("--------- TASK 15 -----------")
myList = [-2, 54, -90, 32, 77, 120]

convertedToTuple = tuple(myList)

print(myList)
print(convertedToTuple)



# Task 16
print("--------- TASK 16 -----------")
myTuple = (1, 2, 3, 4, 5)

sortedTuple = list(myTuple)

sortedTuple.sort()

sortedTuple = tuple(sortedTuple)

if myTuple == sortedTuple:
    print("Given tuple is sorted.")
else:
    print("Given tuple is not sorted.")



# Task 19
print("--------- TASK 19 -----------")
myTuple = (1, 2, 3, 4, 5)
element = 4

newTuple = ()
newList = []

for elem in myTuple:
   if elem != element:
        newList.append(elem)

newTuple = tuple(newList)

print(myTuple)
print(element)
print(newTuple)




# Task 20
print("--------- TASK 20 -----------")
myTuple = (-1, 134, -281, -42, 5, 26, 999)

converted = list(myTuple)

nestedTuple= []

for i in range(len(converted)):
    if i % 2 != 0:
        nestedTuple.append((converted[i-1], converted[i]))

if len(converted) % 2 != 0:
    nestedTuple.append((converted[len(converted)-1], ))

nestedTuple = tuple(nestedTuple)

print(nestedTuple)


# Task 21
print("--------- TASK 21 -----------")
myTuple = (1, 2, 3, 4, 5)
repeatNumber = 3

newTuple = ()
newList = []

for elem in myTuple:
    for i in range(repeatNumber):
        newList.append(elem)

newTuple = tuple(newList)

print(myTuple)
print(newTuple)


# Task 22
print("--------- TASK 22 -----------")
rangeTuple = []

for number in range(10):
    rangeTuple.append(number+1)

rangeTuple = tuple(rangeTuple)

print(rangeTuple)



# Task 23
print("--------- TASK 23 -----------")
myTuple = (1, 2, 3, 4, 5)

reversedTuple = list(myTuple)
reversedTuple.reverse()

reversedTuple = tuple(reversedTuple)

print(myTuple)
print(reversedTuple)


# Task 24
print("--------- TASK 24 -----------")
myTuple = (1, 2, 3, 4, 5, 4, 3, 2)

reversedTuple = list(myTuple)
reversedTuple.reverse()

reversedTuple = tuple(reversedTuple)

print(myTuple)
if myTuple == reversedTuple:
    print("Given tuple is palindrome.")
else:
     print("Given tuple is not palindrome.")


# Task 25
print("--------- TASK 25 -----------")
myTuple = (1, 2, 3, 4, 5, 4, 3, 2)

uniqueElementsTuple = []

for elem in myTuple:
    if uniqueElementsTuple.count(elem) == 0:
        uniqueElementsTuple.append(elem)

uniqueElementsTuple = tuple(uniqueElementsTuple)

print(myTuple)
print(uniqueElementsTuple)