expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    # ADD EXPENSE
    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        note = input("Enter note: ")

        expense = {
            "amount": amount,
            "category": category,
            "note": note
        }

        expenses.append(expense)
        print("✅ Expense added successfully")

    # VIEW EXPENSES
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found")
        else:
            print("\nAll Expenses:")
            for i in expenses:
                print("Amount:", i["amount"],
                      "| Category:", i["category"],
                      "| Note:", i["note"])

    # TOTAL EXPENSE
    elif choice == "3":
        total = 0
        for i in expenses:
            total = total + i["amount"]

        print("💰 Total Expense:", total)

    # EXIT
    elif choice == "4":
        print("👋 Exiting Expense Tracker")
        break

    # INVALID INPUT
    else:
        print("❌ Invalid choice, try again")
