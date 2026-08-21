import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "finance.db")

class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
    


    def connect(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor() 
            print("Database connected successfully")
        except Exception as e:
            print(f"Error: {e}")
        
        try:
            cursor.execute(
            """CREATE TABLE IF NOT EXISTS categories (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL
            ) """)
            cursor.execute(
            """CREATE TABLE IF NOT EXISTS transactions (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL CHECK (type IN ('INCOME', 'EXPENSE')),
            amount FLOAT NOT NULL,
            date DATE NOT NULL,
            description TEXT,
            category_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id)
            ) """) 
            cursor.execute(
            """CREATE TABLE IF NOT EXISTS budget (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER,
            amount FLOAT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id)
            ) """)


            conn.commit()
            print("Table created successfully")
        
        except Exception as e :
            print (f" error: {e}")
  
        return conn




    def viewtable(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor() 
            print("Database connected successfully")
            cursor.execute("SELECT * FROM transactions")
            print(cursor.fetchall())
        except Exception as e:  
            print(f"Error: {e}")



     