string = input("Enter a string: ").lower()

vowelsReplaced = string.replace("a", "*")
vowelsReplaced = vowelsReplaced.replace("e", "*")
vowelsReplaced = vowelsReplaced.replace("i", "*")
vowelsReplaced = vowelsReplaced.replace("u", "*")
vowelsReplaced = vowelsReplaced.replace("o", "*")


print(vowelsReplaced)