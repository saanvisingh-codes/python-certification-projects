def save_expense(item, amount):
    with open("expenses.txt", "a") as file:
        file.write(f"{item},{amount}\n")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Expense name: ")
        amount = float(input("Amount: ₹"))

        save_expense(item, amount)
        print("✅ Expense saved!")

    elif choice == "2":
        try:
            with open("expenses.txt", "r") as file:
                total = 0
                print("\nYour Expenses:")

                for line in file:
                    item, amount = line.strip().split(",")
                    print(f"{item} - ₹{amount}")
                    total += float(amount)

                print(f"\nTotal = ₹{total}")

        except FileNotFoundError:
            print("No expenses found.")

    elif choice == "3":
        try:
            with open("expenses.txt", "r") as file:
                expenses = file.readlines()

            if len(expenses) == 0:
                print("No expenses to delete.")

            else:
                print("\nExpenses:")
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense.strip()}")

                num = int(input("Enter expense number to delete: "))

                if 1 <= num <= len(expenses):
                    expenses.pop(num - 1)

                    with open("expenses.txt", "w") as file:
                        file.writelines(expenses)

                    print("✅ Expense deleted!")

                else:
                    print("Invalid expense number.")

        except FileNotFoundError:
            print("No expenses found.")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
