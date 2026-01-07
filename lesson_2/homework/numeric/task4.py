number1 = int(input("Enter a divident: "))
number2 = int(input("Enter a divider: "))

division, remainder = divmod(number1, number2)

print(f"Result: division = {division} and remainder = {remainder}.")