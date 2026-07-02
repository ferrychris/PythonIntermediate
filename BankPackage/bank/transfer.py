from .balance import balance 

def transfer():
    amount = int(input("enter amount"))
    if  amount < balance():
        return "Error: insufficient balance"
    else:
        return f"transfer amount is {amount} successfully"
        