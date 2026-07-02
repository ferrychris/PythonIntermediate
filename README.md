# Python Intermediate: Modules & Packages

Welcome to my Python Intermediate practice repository! This project is a hands-on learning environment where I practice modular programming, package structures, relative/absolute imports, and interactive command-line interfaces.

---

## 📚 Core Concepts & Theory

### 1. Modules vs. Packages
*   **Module:** A single Python file (`.py`) containing statements, functions, or classes that perform a particular task.
*   **Package:** A folder containing multiple modules grouped together to perform a complete task.
*   **`__init__.py`:** A special file that turns a directory into an importable package, allowing us to easily expose and export modules for external use.
*   **Advantages:** Organizes projects into clean, logical folders, avoids name clashes, and makes code reusable and easy to distribute.

---

## 📂 Repository Structure

Below are the key projects implemented in this repository:

### 🧮 1. Calculator Package (`calculator/`)
A modular calculator demonstration dividing operations into separate files:
*   `maincalculator/add.py` — Addition function.
*   `maincalculator/subtract.py` — Subtraction function.
*   `maincalculator/multiply.py` — Multiplication function.
*   `maincalculator/divide.py` — Division function.
*   `main.py` — Entry point demonstrating how to import and run the calculations.

### 🏫 2. School Package (`schoolPackage/`)
A project showing how to structure entity-based modules:
*   `mainschool/student.py` — Handles student naming.
*   `mainschool/teacher.py` — Handles teacher naming.
*   `mainschool/subject.py` — Handles subject names.
*   `main.py` — Runs and displays school details.

### 🏦 3. Bank Package (`BankPackage/`)
An interactive banking application using the `questionary` library for CLI prompts:
*   `bank/balance.py` — Tracks and returns numeric account balances.
*   `bank/deposit.py` — Handles interactive deposit prompts.
*   `bank/withdraw.py` — Handles numeric validation and withdrawal limits.
*   `bank/transfer.py` — Facilitates fund transfers with balance safety checks.
*   `main.py` — Main entry point hosting the interactive transaction menu.

---

## 🏥 Proposed Future Structure (Hospital System)

As part of package design practice, here is a proposed structure for a modular Hospital System:

```text
HOSPITAL_Package/
├── hospital/
│   ├── __init__.py
│   ├── patient.py
│   ├── Billing.py
│   ├── patientAilment.py
│   ├── Doctors.py
│   ├── Appointment.py
│   └── Pharmacy/
│       ├── __init__.py
│       ├── dispense.py
│       ├── Purchase.py
│       ├── return.py
│       └── Sale.py
└── main.py
```

---

## 🛠️ How to Run the Projects

1. Install the required interactive CLI dependency:
   ```bash
   pip install questionary
   ```
2. Navigate to the desired package and run the main entry point:
   ```bash
   python BankPackage/main.py
   ```
