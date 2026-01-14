# ### **Zero Check Decorator

def div(a, b):
    print(f"input: div({a}, {b})")
    print(f"output: {a/b}")

def decorator(function):
    def wrapper(a, b):
        print("-----------------")
        try:
            function(a, b)
        except ZeroDivisionError:
            print("Denominator can't be zero")
        print("-----------------")

    return wrapper

@decorator
def div(a, b):
    print(f"input: div({a}, {b})")
    print(f"output: {a/b}")


div(10, 2)
div(16, 0)



# ### **Employee Records Manager**

while True:
    menuOption = int(input('''
----------------------------------------
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
Your option: '''))
    
    print("----------------------------------------")

    if menuOption == 6:
        break
    elif menuOption == 1:
        # Employee ID, Name, Position, Salary
        newEmployeeID = input("Enter a new employee ID: ")
        newEmployeeName = input("Enter a new employee name: ")
        newEmployeePosition = input("Enter a new employee position: ")
        newEmployeeSalary = input("Enter a new employee salary: ")

        with open("employees.txt", "+a") as f:
            f.write(f"{newEmployeeID}, {newEmployeeName}, {newEmployeePosition}, {newEmployeeSalary}\n")

        print("\nNew employee added successfully. 🎉\n")
    elif menuOption == 2:
         with open("employees.txt", "+a") as f:
            f.seek(0)

            employeeValues = f.readlines()

            for i in range(len(employeeValues)):
                print(f"{i+1}. "+employeeValues[i].replace("\n", ""))
    elif menuOption == 3:
        with open("employees.txt", "r") as f:
            f.seek(0)
            employeeValues = f.readlines()

            employeeID = input("Enter a employee ID: ")
            foundEmployee = False
            print("\nEmployee Search Result:\n")

            for elem in employeeValues:
                if employeeID in elem:
                    foundEmployee = True
                    print(elem.replace("\n", ""))

            if not foundEmployee:
                print("Employee not found!")
    elif menuOption == 4:
        employeeID = input('Enter a employee ID to update: ')


        with open("employees.txt", "a+") as f:
            f.seek(0)
            employeeValues = f.readlines()
            updatedEmployeeRecord = False

            for i in range(len(employeeValues)):
                if employeeID in employeeValues[i]:
                    employeeName = input("Enter a new employee name: ")
                    employeePosition = input("Enter a new employee position: ")
                    employeeSalary = input("Enter a new employee salary: ")
                    updatedEmployeeRecord = True
                    employeeValues[i] = f"{employeeID}, {employeeName}, {employeePosition}, {employeeSalary}\n"
                    print("\nEmployee record updated successfully. 🎉")
                    break

            f.seek(0)
            f.truncate()
            for elem in employeeValues:
                f.write(elem)


            if not updatedEmployeeRecord:
                print("\nEmployee record not found.")


    elif menuOption == 5:
        employeeID = input('Enter a employee ID: ')

        with open("employees.txt", "a+") as f:
            f.seek(0)
            employeeValues = f.readlines()
            deletedEmployeeRecord = False

            for i in range(len(employeeValues)):
                if employeeID in employeeValues[i]:
                    deletedEmployeeRecord = True
                    employeeValues.remove(employeeValues[i])
                    print("\nEmployee record deleted successfully. 🎉")
                    break

            f.seek(0)
            f.truncate()
            for elem in employeeValues:
                f.write(elem)

            if not deletedEmployeeRecord:
                print("\nEmployee record not found.\n")



### **Word Frequency Counter**

def filterTxt(txt): # Returns String
    return str(txt).translate(str.maketrans("", "", ",./\\|")).replace("  ", " ").lower()

def countWords(txt): # Returns integer
    return len(str(txt).split(" "))


def giveMostFrequentWords(txt, topCommonNumber): # Returns List of Tuples
    dictionary = {}
    splitList = str(txt).split(" ")

    for elem in splitList:
        if dictionary.get(elem) is None:
            dictionary[elem] = 1
        else:
            dictionary[elem] = dictionary[elem]+1

    itemsList = list(dictionary.items())

    itemsList.sort(key=lambda a: a[1], reverse=True)

    return itemsList[:topCommonNumber]


with open("sample.txt", "+r") as f:
    topCommonWordsNumber = int(input("How many top common words do you need? "))
    txt = f.read()

    if txt:
        print(f"Sentence: '{txt}'.")
        filteredTxt = filterTxt(txt=txt)
        countOfWords = countWords(txt=filteredTxt)
        mostFrequent5Words = giveMostFrequentWords(filteredTxt, topCommonWordsNumber)

        print("Word Count Report")
        print(f"Total Words: {countOfWords}")

        for i in range(len(mostFrequent5Words)):
             print(f"{mostFrequent5Words[i][0]} - {mostFrequent5Words[i][1]} times")

    else:
        userInput = input("Enter a sentence: ")

        f.write(userInput)

        f.seek(0)

        txt = f.read()
        print(f"Sentence: '{txt}'.")

        filteredTxt = filterTxt(txt=txt)
        countOfWords = countWords(txt=filteredTxt)
        mostFrequent5Words = giveMostFrequentWords(filteredTxt, topCommonWordsNumber)

        print("Word Count Report")
        print(f"Total Words: {countOfWords}")

        for i in range(len(mostFrequent5Words)):
             print(f"{mostFrequent5Words[i][0]} - {mostFrequent5Words[i][1]} times")




