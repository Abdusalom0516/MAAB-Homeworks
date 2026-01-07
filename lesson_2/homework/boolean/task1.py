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