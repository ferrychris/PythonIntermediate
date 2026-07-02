
import json
import os
import questionary
from questionary import select
from random import randint

students = []


def add_student():
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        students = []
    id = randint(1000, 9999)
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    email = input("Enter your email: ")
    phone = int(input("Enter your phone: "))
    course = input("Enter your course: ")


    student={
        "id":id,
        "name":name,
        "age":age,
        "gender":gender,
        "email":email,
        "phone":phone,
        "course":course
    }
    students.append(student)
    with open("students.json", "w") as f:
        json.dump(students, f, indent=2)
    print(f"Student added successfully {students}")
    student_ops()
# add_student()

def view_students():
     if os.path.exists("students.json"):
        with open("students.json", "r") as f:
            students = json.load(f)
        if students==[]:
            print("No students found")
        else:
            print(students)
        student_ops()
# view_students()

def search():
     if os.path.exists("students.json"):
        with open("students.json", "r") as f:
            students = json.load(f)
        search= input("enter the searchname: ").lower()
        for i in students:
            if i["name"] == search:
                print(i)
                break
        student_ops()


# search()
 
def update():
     if os.path.exists("students.json"):
        with open("students.json", "r") as f:
            students = json.load(f)
        update=input("enter the name you want to update nam: ")
              
        for i in students:
            if i["name"] == update:
               choices=["name","age","gender","email","phone","course"]
               field = questionary.select("What do you want to update?", choices=choices).ask()
               new_value = input(f"Enter new {field}: ")
               i[field] = new_value
               with open("students.json", "w") as f:
                   json.dump(students, f, indent=2)
               print("Student updated successfully!")
               break
            student_ops()

                
              
              
                
def student_ops():
    choices=["add","view","search","update","delete","exit"]
    choice = questionary.select("What do you want to do?", choices=choices).ask()
    if choice=="add":
        add_student()
    elif choice=="view":
        view_students()
    elif choice=="update":
        update()
    elif search == "search":
        search()
    # elif choice=="delete":
    #     delete()
    # elif choice=="exit":
    #     exit()
student_ops()

students = [
    { "name": "alice","age":23, "grade" : { "python":46,"math":90,"chemistry":76}},
    { "name": "bob","age":22, "grade" : { "python":46,"math":90,"chemistry":76}},
    { "name": "charlie","age":21, "grade" : { "python":46,"math":90,"chemistry":76}},
    { "name": "david","age":20, "grade" : { "python":46,"math":90,"chemistry":76}},
    { "name": "eve","age":19, "grade" : { "python":46,"math":90,"chemistry":76}},
    { "name": "frank","age":18, "grade" : { "python":46,"math":90,"chemistry":76}},
    { "name": "grace","age":17, "grade" : { "python":46,"math":90,"chemistry":76}},
    { "name": "helen","age":16, "grade" : { "python":46,"math":90,"chemistry":76}},
    { "name": "ivan","age":15, "grade" : { "python":46,"math":90,"chemistry":76}},
    { "name": "judy","age":14, "grade" : { "python":46,"math":90,"chemistry":76}},


]
# print grade  of python    
for x in students:
    print(x["grade"]["python"])

# save all pthon to a list
# transforming nested Data
data = [{"name":"sam","age":23, 
        "grade":{"math":87,"english":90}}]
new_dict={}
for i in data:
        new_dict["name"]=i["name"]
        new_dict["age"]=i["age"]
        for j in i["grade"]:
            new_dict[j]=i["grade"][j]
            
    print(new_dict)

    flaten_list=[]
    for i in students:
        for j in i["grade"]:
            flaten_list.append(i["name"],i["age"],j,i["grade"][j])