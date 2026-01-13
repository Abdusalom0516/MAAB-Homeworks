# ### **Zero Check Decorator

def div(a, b):
    print(f"input: div({a}, {b})")
    print(f"output: {a/b}")

def decorator(function):
    def wrapper(a, b):
        print("-----------------")
        try:
            function(a, b)
        except ZeroDivisionError:
            print("Denominator can't be zero")
        print("-----------------")

    return wrapper

@decorator
def div(a, b):
    print(f"input: div({a}, {b})")
    print(f"output: {a/b}")


div(10, 2)
div(16, 0)



# ### **Employee Records Manager**
