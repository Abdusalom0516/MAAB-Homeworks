sentence = input("Enter a sentence: ")

splittedList = sentence.split()

result = ""

for i in range(len(splittedList)):
    result = result+splittedList[i][0]

result = result.upper()

print(result)