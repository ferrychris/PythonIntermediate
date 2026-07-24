import sqlite3
from view_task import view_task

def delete_task():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    
    print("Current tasks:")
    view_task()
    
    getexact = input("Enter the id of the task to delete: ")
    
    cursor.execute("DELETE FROM todo WHERE id = ?", (getexact,))
    conn.commit()
    conn.close()
    
    print("Data deleted successfully!")
