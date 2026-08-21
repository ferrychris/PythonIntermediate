import sqlite3
from database.database import DB_PATH

class Transaction:
    def __init__(self, amount, date, description):
        self.amount = amount
        self.date = date
        self.description = description

class Income(Transaction):
    def __init__(self, amount, date, description,category_id):
        super().__init__(amount, date, description)
        self.category_id = category_id

class Expense(Transaction):
    def __init__(self, amount, date, description,category_id):
        super().__init__(amount, date, description)
        self.category_id = category_id

