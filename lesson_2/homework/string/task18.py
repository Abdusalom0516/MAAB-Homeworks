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