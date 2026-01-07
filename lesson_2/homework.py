# Task 1
floatInput = float(input("Enter a floating-point number: "))

print("Rounded value (2 decimal places):", round(floatInput, 2))

# Task 2
number1 = int(input("Enter first number "))
number2 = int(input("Enter second number "))
number3 = int(input("Enter third number "))

if number1 > number2 and number1 > number3:
    if number2 > number3:
        print(f"Largest number is {number1} and smallest number is {number3}")
    else:
        print(f"Largest number is {number1} and smallest number is {number2}")
elif number2 > number1 and number2 > number3:
    if number1 > number3:
         print(f"Largest number is {number2} and smallest number is {number3}")
    else:
        print(f"Largest number is {number2} and smallest number is {number1}")
else:
    print("Damn")
    if number1 > number2:
         print(f"Largest number is {number3} and smallest number is {number2}")
    else:
        print(f"Largest number is {number3} and smallest number is {number1}")




