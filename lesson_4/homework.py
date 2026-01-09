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


# Task 4
print("--------------- Task 4 ----------------")
import random
randomNumber = random.randint(1, 100)
liveCount = 10

while True:
    userGuess = int(input("Enter your guess number: "))

    if userGuess > randomNumber:
        liveCount -= 1
        print(f"Too high! Remaining live count: {liveCount}.")
    elif userGuess < randomNumber:
        liveCount -= 1
        print(f"Too low! Remaining live count: {liveCount}.")
    else:
        print("You guessed it right!")
        break

    if liveCount <= 0:
        userChoise = input(f"You lost. The random numbers was {randomNumber}. Want to play again? ")

        if userChoise == "Y" or userChoise == "YES" or userChoise == "yes" or userChoise == "y" or userChoise == "OK" or userChoise == "ok":
            liveCount = 10
            randomNumber = random.randint(1, 100)
        else:
            break


# Task 5
print("--------------- Task 5 ----------------")
import re

while True:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Password is too short.")
    elif not bool(re.search(f"[A-Z]", password)):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")
        break


# Task 6
print("--------------- Task 6 ----------------")
print("Prime Numbers between 1 and 100.")
for number in range(1, 100+1):
    divisableCount = 0
    for i in range(1, number+1):
        if number % i == 0:
            divisableCount+=1
            if divisableCount > 2:
                break

    if divisableCount == 2:
        print(number)


# Bonus Challange
print("--------------- Bonus Challange ----------------")
import random
userScore = 0
compScore = 0

while True:
    compChoise = random.randint(0, 2)
    userChoise = int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissors: ").strip())

    if compChoise == userChoise:
        print("Draw")
    elif compChoise == 0 and userChoise == 2:
        print("Computer chose Rock you chose Scissors. Computor +1.")
        compScore += 1
    elif compChoise == 0 and userChoise == 1:
        print("Computer chose Rock you chose Paper. User +1.")
        userScore += 1
    elif compChoise == 1 and userChoise == 0:
        print("Computer chose Paper you chose Rock. Computer +1.")
        compScore += 1
    elif compChoise == 1 and userChoise == 2:
        print("Computer chose Paper you chose Scissors. User +1.")
        userScore += 1
    elif compChoise == 2 and userChoise == 0:
        print("Computer chose Scissors you chose Rock. User +1.")
        userScore += 1
    elif compChoise == 2 and userChoise == 1:
        print("Computer chose Scissors you chose Paper. Computer +1.")
        compScore += 1
    else:
        print("You entered invalid value. Computer +1.")
        compScore += 1

    if userScore >= 5:
        print("User won the game.")
        break
    elif compChoise >= 5:
        print("Computer won the game.")
        break








