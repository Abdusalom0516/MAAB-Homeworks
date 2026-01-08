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







