string = input("Enter a string: ")

while len(string) < 2:
    print("String length must be greater or equal to 2.")
    string = input("Enter a string: ")


print(f"First character of {string} is {string[0]} and last charater is {string[len(string)-1]}.")