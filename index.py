# Class is an Object Constructor


class Car:
    x=5

num = Car()
print(num.x)
del num



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

abef= Person("John",30)

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name,"says Ruff Ruff!")

d1 = Dog("Buddy",2)
d1.bark()

class Developer:
    def __init__(self,name,age,language,pay):
        self.name = name
        self.age = age
        self.language = language
        self.pay = pay
    def display_info(self):
        print(self.name,self.age,self.language,self.pay)
    def apply_raise(self,amount):
        self.pay = int(self.pay * amount)
        return(self.pay)

class Employee(Developer):
    def __init__(self,name,age,language,pay,tax_bill):
       super().__init__(name,age,language,pay,)
       self.tax_bill= int(pay *15)



empl1 = Employee("John",30,"Python",800000,100)
print(empl1.apply_raise(1.2))
print(empl1.tax_bill)
# print(empl1.apply_raise)
# print(empl1.pay)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year
    
    def move(self):
        print("Move move!")

class Car(Vehicle):
    def move(self):
        print("Drive!")

class Bus(Vehicle):
    def move(self):
        print("Drive danfo!")

class Ship(Vehicle):
    def move(self):
        print("Sail!")
class Air(Vehicle):
    pass

v1 = Vehicle("Toyota", "Camry", 2020)
v2 = Car("Toyota", "Corolla", 2021)
v3 = Bus("Ibadan Mass Transit", "Bus", 2022)
v4 = Ship("Titanic", "Ship", 2023)
v5 = Air("Boeing", "747", 2024)


v1.move()
v2.move()
v3.move()
v4.move()
v5.move()
        
    
    
