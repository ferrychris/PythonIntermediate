

students = [ 
    {'name':'Alice', 
    'grades':{'math':90,'science':85,'english':88}
    },
    {'name':'Bob','grades':
    {'math':72,'science':80,'english':75}
    },
    {'name':'Charlie','grades':
    {'math':88,'science':92,'english':84}
    } 
]

for student in students:
    student_name=student["name"]
    student_grade=student["grades"]
    for grades in student_grade:
        grade_cal=sum(student_grade.values())/len(grades)
        print (f"{student_name}got an average of {grade_cal}")
        break
        


2. 
products = { 
'name':['Laptop','Phone','Tablet'], 
'price':[1200,800,400], 
'stock':[5,10,7] 
}

conv_tupp =zip(products["name"],products["price"],products["stock"])
for i in conv_tupp:
    print(i)
    print(type(i))
conv_list =list(conv_tupp)
for i in conv_list:
    print(conv_list)
    print(type(i))


