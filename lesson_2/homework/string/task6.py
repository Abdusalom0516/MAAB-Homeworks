string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if string2 in string1:
    print(f"'{string1}' contains '{string2}'.")
else:
    print(f"'{string1}' dosn't contain '{string2}'.");