# ## Model a Farm

class Animal:
    name: str
    color: str
    __gender: str
    price: float

    def __init__(self, *, name: str, color: str, gender: str, price: float):
        self.name = name
        self.color = color
        self.price = price
        self.__gender = gender

    @property
    def gender(self):
        return self.__gender

    def eat(self):
        print(f"{self.__class__.__name__} named {self.name} is eating...")

    def walk(self):
        print(f"{self.__class__.__name__} named {self.name} is walking...")

    def makeNoise(self):
        print(f"{self.__class__.__name__} named {self.name} is making noise...")



class Horse(Animal):
    speed: float
    breed: str

    def __init__(self, *, name: str, color: str, gender: str, price: float, speed: float, breed: str):
        super().__init__(name=name, color=color, gender=gender, price=price)

        self.speed = speed
        self.breed = breed

    def run(self):
        print("Horse is running...")



class Cow(Animal):
    amountMilkPerDay: float
    isPregnant: bool

    def __init__(self, *, name: str, color: str, gender: str, price: float, amountMilkPerDay: float, isPregnant: bool):
        super().__init__(name=name, color=color, gender=gender, price=price)

        self.amountMilkPerDay = amountMilkPerDay
        self.isPregnant = isPregnant

    def produceMilk(self):
        print("Cow is producing milk...")


class Chicken(Animal):
    numberOfEggsPerDay: int

    def __init__(self, *, name: str, color: str, gender: str, price: float, numberOfEggsPerDay: int):
        super().__init__(name=name, color=color, gender=gender, price=price)

        self.numberOfEggsPerDay = numberOfEggsPerDay


    def layEgg(self):
        print("Chicken is laying egg...")




horse = Horse(name="Shadow", color="Black", gender="male", breed="Persian", price=15000, speed=58)
cow = Cow(amountMilkPerDay=35, isPregnant=False, name="Shiny", gender="female", color="Black & White", price=4500)
chicken = Chicken(numberOfEggsPerDay=3, name="Cocky", color="White", gender="female", price=55)

horse.eat()
cow.walk()
chicken.makeNoise()

horse.run()
cow.produceMilk()
chicken.layEgg()






