class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        
    def speak(self):
        return f"{self.name} says Meow!"

# Practice Time!
if __name__ == "__main__":
    my_dog = Dog("Buddy", "Golden Retriever")
    my_cat = Cat("Whiskers", "Orange")

    print(f"I have a {my_dog.breed} named {my_dog.name}.")
    print(my_dog.speak())
    
    print(f"I have an {my_cat.color} cat named {my_cat.name}.")
    print(my_cat.speak())
