expenses = []

while True:
    print("\nWelcome to Expense Tracker, what would you like to do?")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Monthly Expenditure")
    print("5. Exit")

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

        print("\nExpenses List:")

        for expense in expenses:
            print(expense)

    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Spending:", total)

    elif choice == "4":

        month = input("Enter month and year (MM-YYYY): ")

        total = 0

        for expense in expenses:

            expense_month = expense["date"][3:]

            if expense_month == month:
                total += expense["amount"]

        print("Monthly Expenditure:", total)

    elif choice == "5":

        print("Exiting...")
        break

    else:
        print("Invalid Choice")