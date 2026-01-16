class Person:
    name: str
    age: int

    def __init__(self, *, name: str, age: int):
        self.name = name
        self.age = age

    def talk(self):
        print("Hello...")


class Developer(Person):
    salary: float
    department: str

    def __init__(self, *, name: str, age: int, salary: float, department: str):
        super().__init__(name=name, age=age)

        self.salary = salary
        self.department = department

    def work(self):
        print("Working...")

    @property
    def hello(self):
        pass

    @hello.setter
    def hello(self, value):
        pass

# file = 1 model or modul
# package is multipple files or we can say multiple moduls

developer = Developer(name="Abdusalom", age=20, department="IT", salary=2500)

developer.talk()
developer.work()

hello = "hello"

print(f"{hello!r}")


