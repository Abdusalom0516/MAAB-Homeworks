# List Comprehention
numbersList = [1, 2, 3, 4, 5]

evenNumbers = [value for value in numbersList if value % 2 == 0]

print(numbersList)
print(evenNumbers)

print("---------------------")

a = 999
b = f"{a} is even." if a % 2 == 0 else f"{a} is not even."

print(b)


print("---------------------")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

newList = [i for value in matrix for i in value]

print(matrix)
print(newList)