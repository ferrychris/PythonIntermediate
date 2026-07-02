def deposit():
    prompt= input("do you want to deposit? (y/n)").lower()
    if prompt == "y".lower():
        amount = int(input("enter amount: "))
        if amount !=0:
            return f"deposit amount is {amount} successfully"
    elif prompt =="n".lower():
        return "try others"

