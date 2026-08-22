from datetime import datetime

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return True


def validate_description(description):
    if not description or len(description.strip()) == 0:
        raise ValueError("Description cannot be empty")
    return True


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")