# Task 1
print("--------------- Task 1 ----------------")
list1 = [1, 1, 2]
list2 = [2, 3, 4]

uncommonElementsList = []

for elem in list1:
    if elem not in list2:
        uncommonElementsList.append(elem)

for elem in list2:
    if elem not in list1:
        uncommonElementsList.append(elem)

print(uncommonElementsList)


# Task 2
print("--------------- Task 2 ----------------")
n = 7

for i in range(1, n):
    print(i*i)


# Task 3
print("--------------- Task 3 ----------------")
txt = "abcabcdabcdeabcdefabcdefg"
newTxt = ""
unusableChars = ['a', 'e', 'i', 'u', 'o']

count = 0
for i in range(len(txt)-1):
    char = txt[i]
    count+=1
    if count > 2 and char not in unusableChars:
        newTxt += char
        newTxt += "_"
        unusableChars.append(char)
        count = 0
    else:
         newTxt += char


newTxt += txt[len(txt)-1]

print(txt)
print(newTxt)