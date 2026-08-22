from database.database import Database


class FinanceService:
    def __init__(self):
        self.database = Database()

    def add_income(self, amount, date, description):
        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO transactions
            (amount, type, date, description)
            VALUES (?, ?, ?, ?)
        """, (amount, "INCOME", date, description))

        connection.commit()
        connection.close()

        print("Income added successfully!")

    def add_expense(self, amount, date, description):
        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO transactions
            (amount, type, date, description)
            VALUES (?, ?, ?, ?)
        """, (amount, "EXPENSE", date, description))

        connection.commit()
        connection.close()

        print("Expense added successfully!")

    def view_transactions(self):
        connection = self.database.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, type, amount, date, description FROM transactions
        """)
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

        cursor.execute("""
            SELECT b.id, c.name, b.amount FROM budget b
            LEFT JOIN categories c ON b.category_id = c.id
        """)
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
        cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        connection.commit()
        connection.close()
        print("Transaction deleted successfully!")

    def calculate_income(self):
        connection = self.database.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE type = 'INCOME'")
        val = cursor.fetchone()[0]
        connection.close()
        return val or 0.0

    def calculate_expenses(self):
        connection = self.database.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE type = 'EXPENSE'")
        val = cursor.fetchone()[0]
        connection.close()
        return val or 0.0

    def calculate_balance(self):
        return self.calculate_income() - self.calculate_expenses()

    def filter(self, description=None):
        connection = self.database.connect()
        cursor = connection.cursor()
        query = "SELECT id, type, amount, date, description FROM transactions WHERE 1=1"
        params = []
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
