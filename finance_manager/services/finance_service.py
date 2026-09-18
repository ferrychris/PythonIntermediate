from database.database import Database
from utils.session import Session
from utils.validator import validate_expenses

class FinanceService:
    def __init__(self):
        self.database = Database()
   
    def add_income(self, amount, date, description):
        connection = self.database.connect()
        cursor = connection.cursor()
        user_id = Session.get("user_id")

        cursor.execute("""
            INSERT INTO transactions
            (user_id,amount, type, date, description)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, amount, "INCOME", date, description))

        connection.commit()
        connection.close()

        print("Income added successfully!")

    def add_expense(self, amount, date, description):
        connection = self.database.connect()
        cursor = connection.cursor()
        user_id = Session.get("user_id")
        try:
            amount_input = questionary.text("Enter amount: ").ask()
            amount = float(amount_input)
            validate_amount(amount)
            checked_amount = validate_expenses(amount)
            if checked_amount is False:
                print ("\n[Validation Error]You are not a thief!")
                return

            



            today_str = datetime.now().strftime("%Y-%m-%d")
            date = questionary.text("Enter date (YYYY-MM-DD): ", default=today_str).ask()
            validate_date(date)

            description = questionary.text("Enter description: ").ask()
            validate_description(description)

            finance.add_expense(amount, date, description)
        except ValueError as e:
            print(f"\n[Validation Error] {e}\n")
            logger.error(f"Validation error when adding expense: {e}")
        cursor.execute("""
            INSERT INTO transactions
            (user_id,amount, type, date, description)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id,checked_amount, "EXPENSE", date, description))

        connection.commit()
        connection.close()

        print("Expense added successfully!")

    def view_transactions(self):
        connection = self.database.connect()
        cursor = connection.cursor()
        user_id = Session.get("user_id")

        cursor.execute("""
            SELECT id, type, amount, date, description FROM transactions WHERE user_id = ?
        """, (user_id,))
        rows = cursor.fetchall()
        connection.close()

        if not rows:
            print("\nNo transactions found.\n")
            return rows

        print("\n--- Transactions ---")
        for row in rows:
            print(f"ID: {row[0]} | Type: {row[1]} | Amount: ${row[2]} | Date: {row[3]} | Description: {row[4]}")
        print("---------------------\n")
        return rows

    def view_budget(self):
        connection = self.database.connect()
        cursor = connection.cursor()
        user_id = Session.get("user_id")
        cursor.execute("""
            SELECT b.id, c.name, b.amount FROM budget b
            LEFT JOIN categories c ON b.category_id = c.id
            WHERE b.user_id = ?
        """, (user_id,))
        rows = cursor.fetchall()
        connection.close()

        if not rows:
            print("\nNo budget records found.\n")
            return rows

        print("\n--- Budget ---")
        for row in rows:
            cat = row[1] if row[1] else "General"
            print(f"ID: {row[0]} | Category: {cat} | Amount: ${row[2]}")
        print("--------------\n")
        return rows

    def delete_transaction(self, transaction_id):
        connection = self.database.connect()
        cursor = connection.cursor()
        user_id = Session.get("user_id")
        cursor.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (transaction_id, user_id))
        connection.commit()
        connection.close()
        print("Transaction deleted successfully!")

    def calculate_income(self):
        connection = self.database.connect()
        cursor = connection.cursor()
        user_id = Session.get("user_id")
        cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE type = 'INCOME' AND user_id = ?", (user_id,))
        val = cursor.fetchone()[0]
        connection.close()
        return val or 0.0

    def calculate_expenses(self):
        connection = self.database.connect()
        cursor = connection.cursor()
        user_id = Session.get("user_id")
        cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE type = 'EXPENSE' AND user_id = ?", (user_id,))
        val = cursor.fetchone()[0]
        connection.close()
        return val or 0.0

    def calculate_balance(self):
        return self.calculate_income() - self.calculate_expenses()

    def set_budget(self, amount, category_id):
        connection = self.database.connect()
        cursor = connection.cursor()
        user_id = Session.get("user_id")
        cursor.execute("INSERT INTO budget (amount, category_id, user_id) VALUES (?, ?, ?)", (amount, category_id, user_id))
        connection.commit()
        connection.close()
        print("Budget set successfully!")

    def filter(self, description=None):
        connection = self.database.connect()
        cursor = connection.cursor()
        user_id = Session.get("user_id")
        query = "SELECT id, type, amount, date, description FROM transactions WHERE 1=1 AND user_id = ?"
        params = [user_id]
        if description:
            query += " AND description LIKE ?"
            params.append(f"%{description}%")
        cursor.execute(query, params)
        rows = cursor.fetchall()
        connection.close()

        if not rows:
            print("\nNo matching transactions found.\n")
            return rows

        print("\n--- Filtered Transactions ---")
        for row in rows:
            print(f"ID: {row[0]} | Type: {row[1]} | Amount: ${row[2]} | Date: {row[3]} | Description: {row[4]}")
        print("-----------------------------\n")
        return rows
