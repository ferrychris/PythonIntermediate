class Dog:
    def speak(self):
        return "Woof"
        
class Cat:
    def speak(self):
        return "Meow"

def make_anim(test):
    print(test.speak()) 
class Makeup:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def look(self):
        return f"I have {self.name} and it costs {self.price}"
    
    def __str__(self):
        return self.look()
    def __len__(self):
        return len(self.name)
Book = Makeup("Mubeen",34343)
print(len(Book))

    
    # Class for 10/07/2026
#json and request Library
#JsonParsing and Serialiazation

    

        
       