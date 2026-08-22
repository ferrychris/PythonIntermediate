import csv


def export_to_csv(transactions):
    with open("exports/transactions.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Amount",
            "Type",
            "Category",
            "Date",
            "Description"
        ])

        writer.writerows(transactions)

    print("Transaction exported")