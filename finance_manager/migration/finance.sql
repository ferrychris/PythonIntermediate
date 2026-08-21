import sqlite3 conn = sqlite3.connect ("finance.db") cursor = conn.cursor () cursor.execute (
    '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type [INCOME, EXPENSE] NOT NULL,
        amount FLOAT NOT NULL,
        date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
'''
)