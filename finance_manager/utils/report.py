import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT_DIR = os.path.join(BASE_DIR, "exports")
os.makedirs(EXPORT_DIR, exist_ok=True)
EXPORT_FILE = os.path.join(EXPORT_DIR, "transactions.csv")


def export_to_csv(transactions):
    if not transactions:
        print("\nNo transactions available to export.\n")
        return

    with open(EXPORT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "user_id",
            "Type",
            "Amount",
            "Date",
            "Description",
            "category_id"
        ])

        writer.writerows(transactions)

    print(f"\nTransactions exported successfully to {EXPORT_FILE}\n")