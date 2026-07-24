import sqlite3

def view_task():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM todo")
    results = cursor.fetchall()
    
    if not results:
        print("No tasks found.")
    else:
        for row in results:
            print(row)
            
    conn.close()
