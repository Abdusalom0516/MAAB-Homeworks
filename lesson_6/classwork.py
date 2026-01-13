# Generator

def generator():
    yield 1
    yield 2
    yield 3

numbers = generator()

print(next(numbers))
print(next(numbers))
print(next(numbers))


def sayHello(*, name):
    print(f"Hello {name}.")


sayHello(name="Sucker")


def decorator(function):
    def wrapper(*args, **kwargs):
        print("---------------")
        function(*args, **kwargs)
        print("---------------")
    return wrapper


@decorator
def sayHello(*, name):
    print(f"Hello {name}.")


sayHello(name="Sucker")


file = open("/Users/macbookpro/Desktop/MAAB Homeworks/text.txt", mode="r+")

file.write(" Hello, I would love to have a talk with you.")

file.seek(0)

text = file.read()
print(text)

file.close()

# Opening file with Context Manager
with open("/Users/macbookpro/Desktop/MAAB Homeworks/text.txt", mode="r+") as file_explorer:
    file_explorer.write(" Hello, I would love to have a talk with you bitch.")

    file_explorer.seek(0)

    text = file_explorer.read()
    print(text)





