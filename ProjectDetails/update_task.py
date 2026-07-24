import sqlite3
from view_task import view_task

def update_task():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    
    print("Current tasks:")
    view_task()
    
    getexact = input("Enter the id of the task to update: ")
    getnewvalue = input("Enter the new status: ")
    
    cursor.execute("UPDATE todo SET task_status = ? WHERE id = ?", (getnewvalue, getexact))
    conn.commit()
    conn.close()
    
    print("Data updated successfully!")
