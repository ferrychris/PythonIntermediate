Personal Finance Manager (CLI)

A robust, interactive command-line personal finance management application built with Python. It lets you track income and expenses, calculate net balances, filter transactions, manage budgets, log application events, and export records to CSV, all backed by a relational SQLite database.

Features

You can add income and expenses with an amount, date, and description. The app automatically calculates total income, total expenses, and your current net balance. Transactions can be filtered and searched using keyword matching, and you can view a clean, formatted transaction list or delete records by ID. There's a budget overview showing categories and allocated funds, and you can export your full transaction history to exports/transactions.csv for spreadsheet analysis. Input is validated throughout: amounts must be greater than zero, dates must follow the YYYY-MM-DD format, and descriptions can't be empty. Application lifecycle events and errors are logged automatically to logs/app.log. Data is stored in SQLite using foreign keys, data constraints, and parameterized queries.

Project structure

finance_manager/
    database/
        __init__.py
        database.py          SQLite database connection and table schema
    models/
        __init__.py
        transaction.py       OOP data models (Transaction, Income, Expense)
    services/
        __init__.py
        finance_service.py   Business logic: CRUD, balance calculations, filtering
    utils/
        __init__.py
        logger.py            Application logging configuration
        validator.py         Input validation functions (amount, date, description)
        report.py            CSV report exporter
    exports/                 Exported CSV transaction files
        transactions.csv
    logs/                    Application runtime logs
        app.log
    finance.db               SQLite database file
    requirements.txt         Project dependencies
    main.py                  Interactive CLI entry point
    README.md                Project documentation

Tech stack and concepts

Written in Python 3.10+, using SQLite3 for storage and Questionary (https://github.com/tmbo/questionary) for interactive terminal prompts. The architecture follows object-oriented programming with a modular, service-oriented pattern. Logging and CSV export rely on Python's built-in logging and csv libraries.

Installation and setup

Clone the repository:

git clone https://github.com/ferrychris/PythonIntermediate.git
cd PythonIntermediate/finance_manager

Set up a virtual environment.

Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

Windows (Command Prompt):
python -m venv venv
venv\Scripts\activate.bat

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
# or directly install questionary
pip install questionary

How to run

Make sure your virtual environment is active, then run:

python main.py

You'll see a menu with these options: Add Income, Add Expense, View Transactions, View Budget, Filter Transactions, Calculate Balance, Delete Transaction, Export CSV, Exit.

Database schema overview

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL CHECK (type IN ('INCOME', 'EXPENSE')),
    amount FLOAT NOT NULL,
    date DATE NOT NULL,
    description TEXT,
    category_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE IF NOT EXISTS budget (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    amount FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

Author

GitHub: @ferrychris (https://github.com/ferrychris)
Repository: PythonIntermediate (https://github.com/ferrychris/PythonIntermediate.git)
