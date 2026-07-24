import sqlite3

def add_task():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    
    task_description = input("Enter task description: ")
    task_status = input("Enter task status: ")
    task_todo_date = input("Enter task todo date (YYYY-MM-DD): ")
    
    cursor.execute("""
    INSERT INTO todo (
        task_description,
        task_status,
        task_todo_date,
        task_created_date,
        task_updated_date
    )
    VALUES (?, ?, ?, CURRENT_DATE, CURRENT_DATE)
    """, (task_description, task_status, task_todo_date))
    conn.commit()
    conn.close()
    print("Data inserted successfully!")
