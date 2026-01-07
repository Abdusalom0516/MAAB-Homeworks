vowels = ["a", "e", "i", "o", "u"]

consonants = [
    "b", "c", "d", "f", "g",
    "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s",
    "t", "v", "w", "x", "y", "z"
]

string = input("Enter a string: ")

vowelsCount = 0
consonantsCount = 0

for char in string.lower():
    if char in vowels:
        vowelsCount += 1
    elif char in consonants:
        consonantsCount += 1

print(f"The string '{string}' has {vowelsCount} vowels and {consonantsCount} consonants.")