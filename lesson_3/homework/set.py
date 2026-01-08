# Task 1
print("--------- TASK 1 -----------")
set1 = {"freedom", "toji", "nanami"}
set2 = {"anime", "freedom", "one piece"}

newSet = {*(set1 - set2), *(set2 - set1)}

print(set1 - set2)
print(set2 - set1)
print(newSet)


# Task 2
print("--------- TASK 2 -----------")
set1 = {"freedom", "toji", "nanami"}
set2 = {"anime", "freedom", "one piece"}

newSet = set1.intersection(set2)

print(set1)
print(set2)
print(newSet)


# Task 3
print("--------- TASK 3 -----------")
set1 = {"freedom",  "one piece", "obito"}
set2 = {"anime", "freedom", "one piece", "jjk"}

newSet = set1 - set2

print(set1)
print(set2)
print(newSet)


# Task 4
print("--------- TASK 4 -----------")
set1 = {"freedom",  "one piece"}
set2 = {"anime", "freedom", "one piece", "jjk"}

print(set1)
print(set2)

if set1.issubset(set2) or set2.issubset(set1):
    print(True)
else:
    print(False)


# Task 5
print("--------- TASK 5 -----------")
mySet = {"anime", "freedom", "one piece", "jjk"}
element = "jjk"

if element in mySet:
    print("Given element exists in the set.")
else:
    print("Given element doesn't exist in the set.")


# Task 6
print("--------- TASK 5 -----------")
mySet = {"anime", "freedom", "one piece", "jjk", "freedom"}

uniqueElemLength = len(mySet)

print(mySet)
print(uniqueElemLength)


# Task 7
print("--------- TASK 7 -----------")
myList = ["anime", "freedom", "one piece", "jjk", "freedom"]

mySet = set(myList)

print(myList)
print(mySet)


# Task 8
print("--------- TASK 8 -----------")
myList = ["anime", "freedom", "one piece", "jjk", "freedom"]
element = "jjk"

print(myList)
if element in myList:
    myList.remove(element)
    print(element)
    print(myList)
else:
    print("Given element doesn't exist in the set.")


# Task 9
print("--------- TASK 9 -----------")
mySet = {"anime", "freedom", "one piece", "jjk", "freedom"}

print(mySet)
mySet.clear()
print(mySet)


# Task 10
print("--------- TASK 10 -----------")
mySet = {"anime", "freedom", "one piece", "jjk", "freedom"}

if mySet:
    print("Given set is not empty.")
else:
    print("Given set is empty.")



# Task 11
print("--------- TASK 11 -----------")
set1 = {"freedom",  "one piece", "jojo"}
set2 = {"anime", "freedom", "one piece", "jjk"}

newSet = set1.symmetric_difference(set2)

print(set1)
print(set2)
print(newSet)


# Task 12
print("--------- TASK 12 -----------")
set1 = {"freedom",  "one piece", "jojo"}
element = "diavolo"

print(set1)
print(element)
if element in set1:
    print("Given element is already exists in te set.")
else:
    set1.add(element)
    print(set1)


# Task 13
print("--------- TASK 13 -----------")
set1 = {"freedom",  "diavolo", "one piece", "jojo"}
element = "diavolo"

print(set1.pop())


# Task 14
print("--------- TASK 14 -----------")
mySet = {54, 93, 2, 63, -1, 42}

maxNumber = -99999999999999999

for elem in mySet:
    if elem > maxNumber:
        maxNumber = elem

print(mySet)
print(maxNumber)


# Task 15
print("--------- TASK 15 -----------")
mySet = {54, 93, 2, 63, -1, 42}

maxNumber = 99999999999999999

for elem in mySet:
    if elem < maxNumber:
        maxNumber = elem

print(mySet)
print(maxNumber)


# Task 16
print("--------- TASK 16 -----------")
mySet = {54, 93, 2, 63, -1, 42}

evenNumbersSet = set()

for elem in mySet:
    if elem % 2 == 0:
        evenNumbersSet.add(elem)

print(evenNumbersSet)


# Task 17
print("--------- TASK 17 -----------")
mySet = {54, 93, 2, 63, -1, 42}

oddNumbers = set()

for elem in mySet:
    if elem % 2 != 0:
        oddNumbers.add(elem)

print(oddNumbers)



# Task 18
print("--------- TASK 18 -----------")

rangeSet = set()

for i in range(10):
    rangeSet.add(i+1)

print(rangeSet)


# Task 19
print("--------- TASK 19 -----------")
numbersList = [1, 16, 7, 13, 999, 9]
numbersList2 = [1, 999, 42, 5, 3]

mergedSet = set((*set(numbersList), *set(numbersList2)))

print(numbersList)
print(numbersList2)
print(mergedSet)


# Task 20
print("--------- TASK 20 -----------")
set1 = {1, 16, 7, 13, 999, 9}
set2 = {999, 9, 42, 5, 3}

commonSet = set1.intersection(set2)

print(set1)
print(set2)
if not commonSet:
    print("There is no common elements.")
else:
    print(f"There are common elements. {commonSet}.")


# Task 21
print("--------- TASK 21 -----------")
numbersList = [1, 16, 7, 13, 999, 9, 1, 7, 999]

convertToSet = set(numbersList)

print(numbersList)

numbersList = list(convertToSet)

print(numbersList)



# Task 22
print("--------- TASK 22 -----------")
numbersList = [1, 16, 7, 13, 999, 9, 1, 7, 999]

convertToSet = set(numbersList)

uniqueElementsCount = len(convertToSet)

print(numbersList)
print(uniqueElementsCount)



# Task 23
print("--------- TASK 23 -----------")

import random

randomSet = set()

for i in range(10):
    randomSet.add(random.randint(1, 100))

print(randomSet)





