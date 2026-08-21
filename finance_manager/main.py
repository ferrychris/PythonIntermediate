from database.database import Database
from services.finance_service import FinanceService
import questionary

def main():
    db = Database()
    db.connect()

    try:
        db.connect()
        print("Connected to Database")
    except Exception as e:
        print(f"Error: {e}")

    print("""
    Welcome to the Finance Manager
    """)

    # Show Menu
    menu = questionary.select(
        "What would you like to do?",
        choices=[
            "Add Income",
            "Add Expense",
            "View Transactions",
            "View Budget",
            "Exit"
        ]
    ).ask()

    if menu == "Add Income":
        amount = questionary.text("Enter amount: ").ask()
        date = questionary.text("Enter date (YYYY-MM-DD): ").ask()
        description = questionary.text("Enter description: ").ask()
        finance = FinanceService()
        finance.add_income(
            float(amount),
            date,
            description
        )
    elif menu == "Add Expense":
        amount = questionary.text("Enter amount: ").ask()
        date = questionary.text("Enter date (YYYY-MM-DD): ").ask()
        description = questionary.text("Enter description: ").ask()
        finance = FinanceService()
        finance.add_expense(
            float(amount),
            date,
            description
        )
    elif menu == "View Transactions":
        finance = FinanceService()
        finance.view_transactions()
    elif menu == "View Budget":
        finance = FinanceService()
        finance.view_budget()
    elif menu == "Exit":
        exit()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
