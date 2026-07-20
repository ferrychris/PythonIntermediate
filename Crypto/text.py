import sqlite3


conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        course TEXT,
        cgpa REAL
    )
''')

cursor.execute("INSERT INTO students (name, age, course, cgpa) VALUES (?, ?, ?, ?)", ("John", 20, "Computer Science", 3.8))
# fetchall
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()
print(results)

conn.commit()
conn.close()
() whats datatypes


