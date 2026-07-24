import requests
import sqlite3
import json

conn = sqlite3.connect("todo.db")
cursor=conn.cursor()
 
try:
    conn = sqlite3.connect("todo.db")
    print("Data connected")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_description TEXT,
        task_status TEXT,
        task_todo_date TEXT,
        task_created_date DATE,
        task_updated_date DATE
    );
""")

conn.commit()

def insert_task(task_description, task_status, task_todo_date, task_created_date, task_updated_date):
    cursor.execute("""
    INSERT INTO todo (
        task_description,
        task_status,
        task_todo_date,
        task_created_date,
        task_updated_date
    )
    VALUES (
        ?,
        ?,
        ?,
        ?,
        ?
    )
""", (task_description, task_status, task_todo_date, task_created_date, task_updated_date))
    conn.commit()

try:
    if cursor.execute("INSERT INTO todo (task_description, task_status, task_todo_date, task_created_date, task_updated_date) VALUES ('task 1', 'pending', '2022-01-01', '2022-01-01', '2022-01-01')"):
        print("Data inserted successfully!")
except sqlite3.Error as e:
    print(f"Error inserting data: {e}")



insert_task('task_description', 'task_status', 'task_todo_date', 'task_created_date', 'task_updated_date')

def view_tasks():
    cursor.execute("SELECT * FROM todo")
    results = cursor.fetchall()
    print(results)
    conn.commit()

view_tasks()

def delete_tasks():
    cursor.execute("SELECT * FROM TODO")
    results = cursor.fetchall()
    print(results)
    getexact = input("Enter the id of the task to delete: ")
    cursor.execute(f"DELETE FROM TODO WHERE id = {getexact}")
    conn.commit()
    print("Data deleted successfully!")

delete_tasks()

view_tasks()


def update():
    cursor.execute("SELECT * FROM todo")
    results = cursor.fetchall()
    print(results)
    getexact = input("Enter the id of the task to update: ")
    getnewvalue = input("Enter the new value: ")
    cursor.execute("UPDATE todo SET id = {getnewvalue}, WHERE id = {getexact}")
    conn.commit()
    print("Data updated successfully!")