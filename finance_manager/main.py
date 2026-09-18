from database.database import Database
from services.finance_service import FinanceService
from utils.logger import main_logger
from utils.validator import validate_amount, validate_description, validate_date, validate_budget, validate_expenses
import questionary
from utils.report import export_to_csv 
logger = main_logger()
from datetime import datetime
from utils.session import Session


def main():
    db = Database()
    db.connect()
    

    session = Session()
    auth_choice = questionary.select("Authentication:", choices=["Login", "Create User"]).ask()
    if auth_choice == "Login":
        user_id = session.get_session()
    else:
        user_id = session.create_username()

    if not user_id:
        print("Login failed or cancelled.")
        return
    print("""
    Welcome to the Finance Manager
    """)

    menu = questionary.select(
        "What would you like to do?",
        choices=[
            "Set Budget",
            "Add Income",
            "Add Expense",
            "View Transactions",
            "View Budget",
            "Filter Transactions",
            "Calculate Balance",
            "Calculate Expenses",
            "Delete Transaction",
            "Export CSV",
            "Exit"
        ]
    ).ask()

    finance = FinanceService()

    if menu == "Set Budget":
        try:
            budget_amount = float(questionary.text("Enter budget amount: ").ask())
            validate_budget(budget_amount)
            finance.set_budget(budget_amount, category_id=None)
        except ValueError as e:
            print(f"\n[Validation Error] {e}\n")
            logger.error(f"Validation error when setting budget: {e}")

    elif menu == "Add Income":
        try:
            amount_input = questionary.text("Enter amount: ").ask()
            amount = float(amount_input)
            validate_amount(amount)
            today_str = datetime.now().strftime("%Y-%m-%d")
            date = questionary.text("Enter date (YYYY-MM-DD): ", default=today_str).ask()
            validate_date(date)

            description = questionary.text("Enter description: ").ask()
            validate_description(description)

            finance.add_income(amount, date, description)
        except ValueError as e:
            print(f"\n[Validation Error] {e}\n")
            logger.error(f"Validation error when adding income: {e}")
  
    elif menu == "Add Expense":
        try:
            amount_input = questionary.text("Enter amount: ").ask()
            amount = float(amount_input)
            validate_amount(amount)
            validate_expenses(amount)
            pass
            today_str = datetime.now().strftime("%Y-%m-%d")
            date = questionary.text("Enter date (YYYY-MM-DD): ", default=today_str).ask()
            validate_date(date)

            description = questionary.text("Enter description: ").ask()
            validate_description(description)

            finance.add_expense(amount, date, description)
        except ValueError as e:
            print(f"\n[Validation Error] {e}\n")
            logger.error(f"Validation error when adding expense: {e}")
    elif menu == "View Transactions":
        finance.view_transactions()
    elif menu == "View Budget":
        finance.view_budget()
    elif menu == "Filter Transactions":
        desc = questionary.text("Enter description keyword to filter: ").ask()
        finance.filter(description=desc)
    elif menu == "Calculate Balance":
        balance = finance.calculate_balance()
        print(f"\nBalance: ${balance:.2f}\n")
    elif menu == "Calculate Expenses":
        balance = finance.calculate_expenses()
        print(f"\nExpenses: ${balance:.2f}\n")
    elif menu == "Export CSV":
        transactions = finance.view_transactions()
        export_to_csv(transactions)
    elif menu == "Delete Transaction":
        transaction_id = questionary.text("Enter transaction ID: ").ask()
        finance.delete_transaction(transaction_id)
    elif menu == "Exit":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice")
        logger.warning(f"Invalid choice: {menu}")

    logger.info("Application finished")


if __name__ == "__main__":
    main()
