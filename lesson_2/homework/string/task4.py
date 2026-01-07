value =  input("Enter a value: ")

reversedValue = list(value)

reversedValue.reverse()

reversedValue = "".join(reversedValue)

if reversedValue == value:
    print(f"Value: {value} is palindrome.")
else:
    print(f"Value: {value} is not palindrome.")