# Used with Higher Order Function - Sort, map, filter, reduce

double = lambda x: x * 2
add = lambda x, y: x + y
max_val = lambda x, y: x if x > y else y
is_even =lambda x: x % 2 == 1
agecheck = lambda x: "Eligible for voting" if x >= 18 else "Not Eligible for voting"
print(double(5))
print(add(5, 7))
print(max_val(10, 20))
print(is_even(8))
print(agecheck(10))

Fruits =["Apple", "Banana", "French", "Orange", "Mango"] 
Food =("Beans", "Egg", "Bannana", "Eggroll") 
print(Fruits)
print(sorted(Fruits))
Fruits.sort(reverse=True)
print(Fruits)
print(Food)
Food=sorted(Food, reverse=True)
print(Food)


FruitsDictionary={
    "Banana": 5,
    "Apple": 2,
    "Orange": 3,
    "Mango": 1

}


part2= (sorted(FruitsDictionary.items()))
print(part2)