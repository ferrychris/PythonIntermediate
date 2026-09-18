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
            conn.execute("PRAGMA foreign_keys = ON")
            cursor = conn.cursor()
            print("Database connected successfully")

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                type TEXT NOT NULL CHECK (type IN ('INCOME', 'EXPENSE')),
                amount REAL NOT NULL,
                date DATE NOT NULL,
                description TEXT,
                category_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
            """) 

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS budget (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                category_id INTEGER,
                amount REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (category_id) REFERENCES categories(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """)

            # Ensure columns exist if tables were created with earlier schemas
            cursor.execute("PRAGMA table_info(users)")
            user_columns = [col[1] for col in cursor.fetchall()]
            if "username" not in user_columns:
                cursor.execute("DROP TABLE users")
                cursor.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """)

            cursor.execute("PRAGMA table_info(transactions)")
            tx_columns = [col[1] for col in cursor.fetchall()]
            if "user_id" not in tx_columns:
                cursor.execute("ALTER TABLE transactions ADD COLUMN user_id INTEGER REFERENCES users(id)")

            cursor.execute("PRAGMA table_info(budget)")
            bg_columns = [col[1] for col in cursor.fetchall()]
            if "user_id" not in bg_columns:
                cursor.execute("ALTER TABLE budget ADD COLUMN user_id INTEGER REFERENCES users(id)")

            # Remove rows that don't reference a real user (e.g. leftover from before user_id existed)
            cursor.execute("DELETE FROM transactions WHERE user_id IS NULL OR user_id NOT IN (SELECT id FROM users)")
            cursor.execute("DELETE FROM budget WHERE user_id IS NULL OR user_id NOT IN (SELECT id FROM users)")

            conn.commit()
            print("Table created successfully")
        except Exception as e:
            print(f"Error: {e}")

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



     