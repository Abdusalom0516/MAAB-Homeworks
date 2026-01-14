# ### **Zero Check Decorator

# def div(a, b):
#     print(f"input: div({a}, {b})")
#     print(f"output: {a/b}")

# def decorator(function):
#     def wrapper(a, b):
#         print("-----------------")
#         try:
#             function(a, b)
#         except ZeroDivisionError:
#             print("Denominator can't be zero")
#         print("-----------------")

#     return wrapper

# @decorator
# def div(a, b):
#     print(f"input: div({a}, {b})")
#     print(f"output: {a/b}")


# div(10, 2)
# div(16, 0)



# ### **Employee Records Manager**




# while True:
#     menuOption = int(input('''
# 1. Add new employee record
# 2. View all employee records
# 3. Search for an employee by Employee ID
# 4. Update an employee's information
# 5. Delete an employee record
# 6. Exit         :'''))

#     if menuOption == 6:
#         break
#     elif menuOption == 1:
#         with open("employees.txt", "+a") as f:
#             f



# ### **Word Frequency Counter**

def filterTxt(txt): # Returns String
    return str(txt).translate(str.maketrans("", "", ",./\\|")).replace("  ", " ").lower()

def countWords(txt): # Returns integer
    return len(str(txt).split(" "))


def give5MostFrequentWords(txt): # Returns List of Tuples
    dictionary = {}
    splitList = str(txt).split(" ")

    for elem in splitList:
        if dictionary.get(elem) is None:
            dictionary[elem] = 1
        else:
            dictionary[elem] = dictionary[elem]+1

    return list(dictionary.items())[:5]


with open("sample.txt", "+r") as f:
    txt = f.read()

    if txt:
        filteredTxt = filterTxt(txt=txt)
        countOfWords = countWords(txt=filteredTxt)
        mostFrequent5Words = give5MostFrequentWords(filteredTxt)

        print("Word Count Report")
        print(f"Total Words: {countOfWords}")

        for i in range(len(mostFrequent5Words)):
             print(f"{mostFrequent5Words[i][0]} - {mostFrequent5Words[i][1]} times")

    else:
        userInput = input("Enter a sentence: ")

        f.write(userInput)

        f.seek(0)

        txt = f.read()

        filteredTxt = filterTxt(txt=txt)
        countOfWords = countWords(txt=filteredTxt)
        mostFrequent5Words = give5MostFrequentWords(filteredTxt)

        print("Word Count Report")
        print(f"Total Words: {countOfWords}")

        for i in range(len(mostFrequent5Words)):
             print(f"{mostFrequent5Words[i][0]} - {mostFrequent5Words[i][1]} times")




