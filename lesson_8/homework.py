# ## Model a Farm

class Animal:
    name: str
    color: str
    gender: str
    price: float

    def __init__(self, *, name: str, color: str, gender: str, price: float):
        self.name = name
        self.color = color
        self.price = price
        self.gender = gender

    def eat(self):
        print(f"{type(self)} named {self.name} is eating...")

    def walk(self):
        print(f"{type(self)} named {self.name} is walking...")

    def makeNoise(self):
        print(f"{type(self)} named {self.name} is making noise...")



class Horse(Animal):
    speed: float
    breed: str

    def __init__(self, *, name: str, color: str, gender: str, price: float, speed: float, breed: str):
        super().__init__(name=name, color=color, gender=gender, price=price)

        self.speed = speed
        self.breed = breed




