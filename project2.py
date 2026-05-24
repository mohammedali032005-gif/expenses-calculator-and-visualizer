import matplotlib.pyplot as plt

expenses = []
#hi this is a code
while True:

    print("\n1. Add Expense")
    print("2. Monthly Expense Report")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category: ")
        amount = int(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense Added!")

    elif choice == "2":

        monthly_totals = {}

        print("\nMonthly Expense Details:\n")

        for expense in expenses:

            month = expense["date"][3:]

            if month in monthly_totals:
                monthly_totals[month] += expense["amount"]

            else:
                monthly_totals[month] = expense["amount"]

            print(
                month,
                "->",
                expense["category"],
                ":",
                expense["amount"]
            )

        plt.bar(
            monthly_totals.keys(),
            monthly_totals.values()
        )

        plt.title("Monthly Expenses")

        plt.xlabel("Month")
        plt.ylabel("Amount")

        plt.show()

    elif choice == "3":

        print("Exiting...")
        break

    else:
        print("Invalid Choice")