# Defining a class and creating an object
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        print(f"{self.name} is a {self.species}.")

dog = Animal("Buddy", "dog")
dog.describe()

# Instance fs. class attributes
class circle:
    pi = 3.14159
    def __init__(self, radius):
        self.radius =radius

    def area(self):
        return circle.pi * self.radius ** 2
    
circle1 = circle(5)
print("Area of circle:", circle1.area())

# Inheritance
class fehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def describe(self):
        print(f"This is a {self.brand} fehicle with {self.wheels} wheels.")

class car(fehicle):
    def __init__(self, brand, wheels, doors):
        super().__init__(brand, wheels)
        self.doors = doors

    def describe(self):
        super().describe()
        print(f"It has {self.doors} doors.")

my_car = car("Toyota", 4, 4)
my_car.describe()

# Encapsulation
class bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
 
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}. New balance: {self.__balance}")
        else:
            print(f"Insufficient funds or infalid amount.")

    def get_balance(self):
        return self.__balance

account = bankaccount("Joel", 1000)
account.deposit(500)
account.withdraw(300)
print("Final Balance:", account.get_balance())
