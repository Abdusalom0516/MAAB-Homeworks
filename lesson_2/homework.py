# Boolean Tasks

# Task 1
username = input("Enter a username: ")
password = input("Enter a password: ")

isUsernameNotEmpty = False
isPasswordNotEmpty = False

if username:
    isUsernameNotEmpty = True

if password:
    isPasswordNotEmpty = True

if isUsernameNotEmpty and isPasswordNotEmpty:
    print(True)
else:
    print(False)


# Task 2
number1 = int(input("Enter a number1: "))
number2 = int(input("Enter a number2: "))

print(number1 == number2)


# Task 3
number = int(input("Enter a number: "))

if number % 2 == 0 and number > 0:
    print(True)
else:
    print(False)


# Task 4
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 != number2 and number2 != number3 and number1 != number3:
    print(True)
else:
    print(False)


# Task 5
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if len(string1) == len(string2):
    print(True)
else: 
    print(False)


# Task 6
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(True)
else:
    print(False)


# Task 7
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if number1 + number2 > 50.8:
    print(True)
else:
    print(False)


# Task 8
number1 = int(input("Enter first number: "))

if number1 > 9 and number1 < 21:
    print(True)
else:
    print(False)



# Numeric Tasks

# Task 1
floatInput = float(input("Enter a floating-point number: "))

print("Rounded value (2 decimal places):", round(floatInput, 2))


# Task 2
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 > number2 and number1 > number3:
    if number2 > number3:
        print(f"Largest number is {number1} and smallest number is {number3}.")
    else:
        print(f"Largest number is {number1} and smallest number is {number2}.")
elif number2 > number1 and number2 > number3:
    if number1 > number3:
         print(f"Largest number is {number2} and smallest number is {number3}.")
    else:
        print(f"Largest number is {number2} and smallest number is {number1}.")
else:
    print("Damn")
    if number1 > number2:
         print(f"Largest number is {number3} and smallest number is {number2}.")
    else:
        print(f"Largest number is {number3} and smallest number is {number1}.")


# Task 3
kilometer = int(input("Enter kilometer: "))

print(f"{kilometer}km is {kilometer * 1000}m and {kilometer * 100000}cm.")


# Task 4
number1 = int(input("Enter a divident: "))
number2 = int(input("Enter a divider: "))

division, remainder = divmod(number1, number2)

print(f"Result: division = {division} and remainder = {remainder}.")


# Task 5
celcious = float(input("Enter Celcious: "))

fahrenheit = celcious * 9/5 + 32

print(f"Celcious {celcious} is {fahrenheit} Fahrenheit.")


# Task 6
number = input("Enter a number: ")

print(f"Last digit of {number} is {number[-1]}.")


# Task 7
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"Number {number} is even.")
else:
    print(f"Number {number} is odd.")



# String Tasks

# Task 1
userName = input("Enter your name: ")
userYearOfBirth = int(input("Enter year of birth: "))

print(f"{userName} you are {2026 - userYearOfBirth} years old.")


# Task 3
value = input('Enter a value: ')

length = len(value)
uppercase = value.upper()
lowercase = value.lower()

print(f"Value: {value}, length: {length}, uppercase: {uppercase} and lowercase: {lowercase}.")


# Task 4
value =  input("Enter a value: ")

reversedValue = list(value)

reversedValue.reverse()

reversedValue = "".join(reversedValue)

if reversedValue == value:
    print(f"Value: {value} is palindrome.")
else:
    print(f"Value: {value} is not palindrome.")


# Task 5
vowels = ["a", "e", "i", "o", "u"]

consonants = [
    "b", "c", "d", "f", "g",
    "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s",
    "t", "v", "w", "x", "y", "z"
]

string = input("Enter a string: ")

vowelsCount = 0
consonantsCount = 0

for char in string.lower():
    if char in vowels:
        vowelsCount += 1
    elif char in consonants:
        consonantsCount += 1

print(f"The string '{string}' has {vowelsCount} vowels and {consonantsCount} consonants.")


# Task 6
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if string2 in string1:
    print(f"'{string1}' contains '{string2}'.")
else:
    print(f"'{string1}' dosn't contain '{string2}'.");


# Task 7
sentence = input("Enter a sentence: ")
wordToReplace = input("Replace: ")
replaceWith = input("With: ")


replacedSentence = sentence.replace(wordToReplace, replaceWith)

print(replacedSentence)


# Task 8
string = input("Enter a string: ")

while len(string) < 2:
    print("String length must be greater or equal to 2.")
    string = input("Enter a string: ")


print(f"First character of {string} is {string[0]} and last charater is {string[len(string)-1]}.")


# Task 9
string = input("Enter a string: ")

splittedString = list(string)

splittedString.reverse()

joinedString = "".join(splittedString)

print(joinedString)


# Task 10
sentence = input("Enter a sentence: ")

print(len(sentence.split()))


# Task 11
value = input("Enter a value: ")

if "1" in value or "2" in value or "3" in value or "4" in value or "5" in value or "6" in value or "7" in value or "8" in value or "9" in value or "0" in value:
    print(f"Value: '{value}' contains digit.")
else:
    print(f"Value: '{value}' doesn't contain digits.")


# Task 12
value = input("Enter value: ")

joinedValue = "-".join(value.split())

print(joinedValue)


# Task 13
value = input("Enter value: ")

removedSpaceValue = value.replace(" ", "")

print(removedSpaceValue)


# Task 14
firstValue = input("Enter first value: ")
secondValue = input("Enter second value: ")


if firstValue == secondValue:
    print("Given values are equal.")
else:
    print("Given values are not equal.")


# Task 15
sentence = input("Enter a sentence: ")

splittedList = sentence.split()

result = ""

for i in range(len(splittedList)):
    result = result+splittedList[i][0]

result = result.upper()

print(result)


# Task 16
string = input("Enter a string: ")
char = input("Enter a character: ")

removedString = string.replace(char, "")

print(removedString)


# Task 17
string = input("Enter a string: ").lower()

vowelsReplaced = string.replace("a", "*")
vowelsReplaced = vowelsReplaced.replace("e", "*")
vowelsReplaced = vowelsReplaced.replace("i", "*")
vowelsReplaced = vowelsReplaced.replace("u", "*")
vowelsReplaced = vowelsReplaced.replace("o", "*")

print(vowelsReplaced)


# Task 18
string = input("Enter a string: ")
startsWithInput = input("Starts with: ")
endsWithInput = input("Ends with: ")

isStartsWith = string.startswith(startsWithInput)

isEndsWith = string.endswith(endsWithInput)

if isStartsWith:
    if isEndsWith:
        print(f"String: '{string}' starts with '{startsWithInput}' and ends with '{endsWithInput}'.")
    else:
        print(f"String: '{string}' starts with '{startsWithInput}' but doesn't end with '{endsWithInput}'.")
else:
    if isEndsWith:
        print(f"String: '{string}' doesn't start with '{startsWithInput}' but ends with '{endsWithInput}'.")
    else:
         print(f"String: '{string}' doesn't start with '{startsWithInput}' and doesn't end with '{endsWithInput}'.")


