from datetime import datetime
from database.database import Database
from utils.session import Session

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return True

def validate_budget(budget):
    if budget <= 0:
        raise ValueError("Budget must be positive")
    connection = Database().connect()
    cursor = connection.cursor()
    cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE user_id = ? AND type = 'INCOME'", (Session.get("user_id"),))
    income = cursor.fetchone()[0] or 0.0
    connection.close()
    if budget > income:
        raise ValueError("na thief u be! Spend From what u have!")
    return True

def validate_description(description):
    if not description or len(description.strip()) == 0:
        raise ValueError("Description cannot be empty")
    return True

def validate_balance_check(balance):
    if balance < 0:
        raise ValueError("Balance cannot be negative")
    return True

def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

def validate_expenses(amount):
    connection = Database().connect()
    cursor = connection.cursor()
    cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE user_id = ? AND type = 'INCOME'", (Session.get("user_id"),))
    income = cursor.fetchone()[0] or 0.0
    cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE user_id = ? AND type = 'EXPENSE'", (Session.get("user_id"),))
    expenses = cursor.fetchone()[0] or 0.0
    connection.close()
    if amount > (income - expenses):
        raise ValueError("na thief u be! Spend From what u have!")
    return True