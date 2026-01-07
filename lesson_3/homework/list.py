# Task 1
print("--------- TASK 1 -----------")
list = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
element = "freedom"

elementCount = list.count(element)

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

list = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
element = "freedom"

if element in list:
    print(True)
else:
    print(False)


# Task 6
print("---------- TASK 6 -----------")

list = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

if not list:
    print("List is empty")
else:
    print(list[0])


# Task 7
print("---------- TASK 7 -----------")

list = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

if not list:
    print("List is empty")
else:
    print(list[len(list)-1])


# Task 8
print("---------- TASK 8 -----------")

list = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]
slicedList = list[0:3]

print(slicedList)

# Task 9
print("---------- TASK 9 -----------")

list = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

reversedList = list.copy()

reversedList.reverse()

print(reversedList)


# Task 10
print("---------- TASK 10 -----------")

list = ["Abdusalom", "freedom", "999", "freedom", "The World", "jojo", "Anime"]

sortedList = list.copy()

sortedList.sort()

print(sortedList)



