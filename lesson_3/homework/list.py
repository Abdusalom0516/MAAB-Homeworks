# Task 1
print("--------- TASK 1 -----------")
myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
element = "freedom"

elementCount = myList.count(element)

print(elementCount)


# Task 2
print("---------- TASK 2 -----------")
numbersList = [16, 15, 7, 13, 5, 14]

numbersSum = 0

for number in numbersList:
    numbersSum+=number

print(numbersSum)


# Task 3
print("---------- TASK 3 -----------")
numbersList = [1, 15, 7, 13, 5, 14]

numbersList.sort(reverse=True)

maxElement = numbersList[0]

print(maxElement)


# Task 4
print("---------- TASK 4 -----------")

numbersList = [1, 15, 7, 13, 5, 14]

numbersList.sort()

minElement = numbersList[0]

print(minElement)


# Task 5
print("---------- TASK 5 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
element = "freedom"

if element in myList:
    print(True)
else:
    print(False)


# Task 6
print("---------- TASK 6 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

if not myList:
    print("List is empty")
else:
    print(myList[0])


# Task 7
print("---------- TASK 7 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

if not myList:
    print("List is empty")
else:
    print(myList[len(myList)-1])


# Task 8
print("---------- TASK 8 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
slicedList = myList[0:3]

print(slicedList)

# Task 9
print("---------- TASK 9 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

reversedList = myList.copy()

reversedList.reverse()

print(reversedList)


# Task 10
print("---------- TASK 10 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

sortedList = myList.copy()

sortedList.sort()

print(sortedList)


# Task 11
print("---------- TASK 11 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

duplicateRemovedList = list(set(myList.copy()))

print(duplicateRemovedList)


# Task 12
print("---------- TASK 12 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
element = "Joestar"
index = 7

myList.insert(5, element)

print(myList)


# Task 13
print("---------- TASK 13 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
element = "freedom"

indexOfElement = myList.index(element)

print(indexOfElement)


# Task 14
print("---------- TASK 14 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
myList2 = []

if not myList:
    print(True)
else: 
     print(False)

if not myList2:
    print(True)
else: 
     print(False)


# Task 15
print("---------- TASK 15 -----------")

numbersList = [1, 16, 7, 13, 26, 14]
evenNumbersCount = 0

for number in numbersList:
    if number % 2 == 0:
        evenNumbersCount+=1

print(evenNumbersCount)



# Task 16
print("---------- TASK 16 -----------")

numbersList = [1, 16, 7, 13, 26, 14, 9]
oddNumbersCount = 0

for number in numbersList:
    if number % 2 != 0:
        oddNumbersCount+=1

print(oddNumbersCount)



# Task 17
print("---------- TASK 17 -----------")

numbersList = [1, 16, 7, 13, 26, 14, 9]
myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

combinedList = []

combinedList.extend(numbersList.copy())
combinedList.extend(myList.copy())

print(combinedList)


# Task 18
print("---------- TASK 18 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

sublist = ["freedom", "999", "freedom"]

if "".join(sublist) in "".join(myList):
    print(True)
else:
    print(False)


# Task 19
print("---------- TASK 19 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
element = "freedom"
replacementElement = "Jotaro"

for i in range(len(myList)):
    if myList[i] == element:
        myList[i] = replacementElement
        break

print(myList)


# Task 20
print("---------- TASK 20 -----------")

numbersList = [1, 16, 7, 13, 26, 14, 9]

numbersList = list(set(numbersList))

numbersList.sort(reverse=True)

secondLargest = numbersList[1]

print(f"Second largest number in {numbersList} is {secondLargest}.")



# Task 21
print("---------- TASK 21 -----------")

numbersList = [1, 16, 7, 13, 26, 14, 9]

numbersList = list(set(numbersList))

numbersList.sort()

secondSmallest = numbersList[1]

print(f"Second smallest number in {numbersList} is {secondSmallest}.")


# Task 22
print("---------- TASK 22 -----------")

numbersList = [1, 16, 7, 13, 26, 14, 9]

evenNumbers = []

for number in numbersList:
    if number % 2 == 0:
        evenNumbers.append(number)

print(evenNumbers)


# Task 23
print("---------- TASK 23 -----------")

numbersList = [1, 16, 7, 13, 26, 14, 9]

oddNumbers = []

for number in numbersList:
    if number % 2 != 0:
        oddNumbers.append(number)

print(oddNumbers)



# Task 24
print("---------- TASK 24 -----------")

numbersList = [1, 16, 7, 13, 26, 14, 9]

listLength = len(numbersList)

print(numbersList)
print(listLength)


# Task 25
print("---------- TASK 25 -----------")

numbersList = [1, 16, 7, 13, 26, 14, 9]

copyList = numbersList.copy()

print(numbersList)
print(copyList)


# Task 26
print("---------- TASK 26 -----------")

numbersList = [1, 16, 7, 13, 999, 26, 14, 9]

middleElement = 0
lengthOfList = len(numbersList)


if lengthOfList % 2 == 0:
    middleElement = [numbersList[lengthOfList // 2-1], numbersList[lengthOfList // 2]]
else:
    middleElement = numbersList[lengthOfList // 2]

print(f"Middle element of {numbersList} is {middleElement}.")


# Task 29
print("---------- TASK 29 -----------")

numbersList = [1, 16, 7, 13, 999, 26, 14, 9]
index  = 5

print(numbersList)

numbersList.pop(index)

print(numbersList)



# Task 30
print("---------- TASK 30 -----------")

numbersList = [1, 16, 7, 13, 999, 26, 14, 9]
numbersList2 = [1, 2, 3, 4, 5]

numbersListSorted = numbersList.copy()
numbersList2Sorted = numbersList2.copy()

numbersListSorted.sort()
numbersList2Sorted.sort()

if numbersList == numbersListSorted:
    print(f"{numbersList} is sorted.")
else:
    print(f"{numbersList} is not sorted.")

if numbersList2 == numbersList2Sorted:
    print(f"{numbersList2} is sorted.")
else:
    print(f"{numbersList2} is not sorted.")



# Task 31
print("---------- TASK 31 -----------")

numbersList = [1, 16, 7, 13, 999, 26, 14, 9]
repeatTime = 3

newList = []


for number in numbersList:
    for i in range(repeatTime):
        newList.append(number)

print(numbersList)
print(newList)



# Task 32
print("---------- TASK 32 -----------")

numbersList = [1, 16, 7, 13, 999, 26, 14, 9]
numbersList2 = [1, 134, 281, 42, 5]

mergedSortedList = []

mergedSortedList.extend(numbersList.copy())
mergedSortedList.extend(numbersList2.copy())

mergedSortedList.sort()

print(numbersList)
print(numbersList2)
print(mergedSortedList)



# Task 33
print("---------- TASK 33 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
element = "freedom"

indices = []

for i in range(len(myList)):
    if myList[i] == element:
        indices.append(i)

print(myList)
print(element)
print(indices)



# Task 34
print("---------- TASK 34 -----------")

myList = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

rotatedList = myList.copy()

removedElement = rotatedList.pop()

rotatedList.insert(0, removedElement)

print(myList)
print(rotatedList)


# Task 35
print("---------- TASK 35 -----------")

rangeList = []

for number in range(10):
    rangeList.append(number+1)

print(rangeList)



# Task 36
print("---------- TASK 36 -----------")

numbersList = [-1, 134, -281, -42, 5, 26]

positiveNumsSum = 0

for number in numbersList:
    if number > 0:
        positiveNumsSum+=number

print(numbersList)
print(positiveNumsSum)



# Task 37
print("---------- TASK 37 -----------")

numbersList = [-1, 134, -281, -42, 5, 26]

negativeNumsSum = 0

for number in numbersList:
    if number < 0:
        negativeNumsSum+=number

print(numbersList)
print(negativeNumsSum)



# Task 38
print("---------- TASK 38 -----------")

myList = ["Hello", "Damn", "Hello"]

reversedList = myList.copy()

reversedList.reverse()

print(myList)
print(reversedList)

if myList == reversedList:
    print(True)
else:
    print(False)



# Task 39
print("---------- TASK 39 -----------")

numbersList = [-1, 134, -281, -42, 5, 26, 999]

nestedList = []

for i in range(len(numbersList)):
    if i % 2 != 0:
        nestedList.append([numbersList[i-1], numbersList[i]])

if len(numbersList) % 2 != 0:
    nestedList.append([numbersList[len(numbersList)-1]])

print(nestedList)



# Task 40
print("---------- TASK 40 -----------")

numbersList = [1, 134, -281, 999, 1, -281, -42, 5, 26, 999]

uniqueElements = []

for elem in numbersList:
    countOfElem = uniqueElements.count(elem)

    if countOfElem == 0:
        uniqueElements.append(elem)


print(numbersList)
print(uniqueElements)
