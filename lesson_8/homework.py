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




# ## Build a Bank Application
import uuid

class Account:
    accountNumber: str
    name: str
    balance: float

    def __init__(self, *,  accountNumber: str, name: str, balance: float):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account(accountNumber: {self.accountNumber}, name: {self.name}, balance: {format(self.balance, ',')})"


class Bank:
    accounts: dict[str, Account]

    def __init__(self, *, accounts: dict[str, Account]):
        self.accounts = accounts


    def createAccount(self, *, name: str, initialDeposit: float):
        uid = str(uuid.uuid4())
        print(uid)
        self.accounts[uid] = Account(accountNumber=uid, name=name, balance=initialDeposit)
        print("\nAccount created succesfully 🎉")

        for elem in self.accounts.values():
            print(elem)


    def viewAccount(self, *, accountNumber: str):
        account = self.accounts.get(accountNumber)

        if account == None:
            print("\nAccount not found!")
        else:
            print(account)


    def deposit(self, *, accountNumber: str, amount: float):
        account = self.accounts.get(accountNumber)

        if account == None:
            print("\nAccount not found!")
        else:
            self.accounts[accountNumber].balance = self.accounts[accountNumber].balance+amount
            print("\nDeposit done ✅")


    def withdraw(self, *, accountNumber: str, amount: float):
        account = self.accounts.get(accountNumber)

        if account == None:
            print("\nAccount not found!")
        else:
            availableAmount = account.balance

            if availableAmount >= amount:
                self.accounts[accountNumber].balance = account.balance-amount
                print("\Withdraw done ✅")
            else:
                print("Not enough amount to withdraw!")



bank = Bank(accounts=dict())


while True:
    userOption = input('''
----------------------------------
Welcome Employee Record Manager Application!
# 1. Create account
# 2. View Account
# 3. Deposit
# 4. Withdraw
# 5. Exit
# Your option: ''')

    if userOption == "5":
        break
    elif userOption == "1":
        print("\n")
        accountName = input("Enter account name: ")
        accountInitialDeposit = float(input("Enter initial deposit: "))

        bank.createAccount(name=accountName, initialDeposit=accountInitialDeposit)
    elif userOption == "2":
        print("\n")
        accountNumber = input("Enter account number: ")

        bank.viewAccount(accountNumber=accountNumber)
    elif userOption == "3":
        print("\n")
        accountNumber = input("Enter account number: ")
        amount = float(input("Enter amount: "))

        bank.deposit(accountNumber=accountNumber, amount=amount)
    elif userOption == "4":
        print("\n")
        accountNumber = input("Enter account number: ")
        amount = float(input("Enter amount: "))

        bank.withdraw(accountNumber=accountNumber, amount=amount)
    else:
        print("Invalid Option!")


