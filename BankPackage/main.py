from bank import *
import questionary

# print(balance())
# print(deposit())
# print(transfer())
# print(withdraw())

def transactions():
    choice = questionary.select(
        "What Do You want to Do today?",
        choices=[
            "Balance",
            "Deposit",
            "Transfer",
            "Withdraw"
        ]
    ).ask()

    if choice == "Balance":
        print(balance())
    elif choice == "Deposit":
        print(deposit())
    elif choice == "Transfer":
        print(transfer())
    elif choice == "Withdraw":
        print(withdraw())

transactions()