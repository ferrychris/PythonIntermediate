from .balance import balance 

def withdraw():
    amount = int(input("enter amount: "))
    bal = balance()
    if amount > bal:
        return "Error: insufficient balance"
    else:
        return f"withdraw amount is {amount} successfully"

