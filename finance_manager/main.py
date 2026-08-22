from database.database import Database
from services.finance_service import FinanceService
from utils.logger import main_logger
from utils.validator import validate_amount, validate_description, validate_date
import questionary

logger = main_logger()


def main():
    db = Database()
    db.connect()

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
            "Filter Transactions",
            "Calculate Balance",
            "Delete Transaction",
            "Exit"
        ]
    ).ask()

    finance = FinanceService()

    if menu == "Add Income":
        try:
            amount_input = questionary.text("Enter amount: ").ask()
            amount = float(amount_input)
            validate_amount(amount)

            date = questionary.text("Enter date (YYYY-MM-DD): ").ask()
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

            date = questionary.text("Enter date (YYYY-MM-DD): ").ask()
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
