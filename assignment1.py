class Student:
   def __init__ (self,name,age,course):
    self.name = name
    self.age = age
    self.course = course

abbey= Student("Abbey",23,"Computer Science")
samuel=Student("Samuel",23,"Computer Science")
print(abbey.name)
    # Question 2

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(self.brand)
        print(self.model)
        print(self.year)
Car1 = Car("Passat ", "Volkswagen", 2022)
Car1.display_info()

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name)
        print(self.age)
Dog1= Dog("Tommy",2)
Dog1.bark()

# Question4
class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name=account_name
        self.balance= balance
    def withdraw(self):
        amount = int(input("Enter amount to withdraw"))
        available_balance= self.balance- amount
        print(available_balance)


# Question 5
    
    