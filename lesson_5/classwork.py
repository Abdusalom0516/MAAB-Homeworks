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


# Functions

def greetings(name):
    print(f"Hello {name}.")

greetings("Abdusalom")

# Positionan Paramater
def userGreeting(name, age, /, email, *, surname):
    print(f"Hello {name}{surname}. So you are {age} years old. Email: {email}.")

# / if I use that then I can give the argument in keyworkd form of just positional but if I use * I must give the keyword

userGreeting("Abdusalom", 20, email="abdusalom.gmail.com", surname="G'ayratov")



# def hello():
#     print("Hello")

# def hello(*, name):
#     print(f"Hello {name}.")


# hello()
# hello(name="Jotaro")

# Infinite arguments here
def sumFunction(*numbers):
    print(sum(numbers))


sumFunction(1, 2, 3, 4, 5) # the values becomes tuple 

# Infinite keyword arguments
def addNumbers(**kwargs):
    sumOfNumbers = 0
    for value in kwargs.values():
        sumOfNumbers += value
    print(sumOfNumbers)

addNumbers(a=1, b=2, c=3, d=14) # the values becomes dictionary


print("---------- Lambda Expression ------------");
# Lambda Expression

square = lambda a: a**2

print(square(9))







