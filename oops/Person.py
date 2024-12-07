from datetime import datetime


class Person:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def calculate_birth_year(self):
        print(f"The birth year of {self.name} is {datetime.now().year - self.age}")


class Car(Person):
    def __init__(self, name, age, color, model, make, price):
        super().__init__(name, age, color)
        self.model = model
        self.make = make
        self.price = price

    def displayCar(self):
        print(f"{self.name}, age {self.age}, owns a car of {self.make}, {self.model}")

    def displayPrice(self):
        print(f"Car is priced at {self.price}")


Ann = Car("Ann", 24, "yellow", "indigo cs","tata", 2400000)
Alex = Car("Alex", 30, "yellow", "indigo cs","tata", 2400000)
Sam = Car("Sam", 24, "yellow", "indigo cs","tata", 2400000)
Ann.calculate_birth_year()
Ann.displayCar()
Ann.displayPrice()
