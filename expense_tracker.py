def add_expense(name, amount):
    with open("expenses.txt", "a") as file:
        file.write(f"{name},{amount}\n")


def show_expenses():
    print("\n💰 Your Expenses")

    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

            if not expenses:
                print("No expenses recorded.")
                return

            total = 0

            for expense in expenses:
                name, amount = expense.strip().split(",")
                amount = float(amount)

                print(f"• {name}: ₹{amount}")
                total += amount

            print(f"\nTotal: ₹{total}")

    except FileNotFoundError:
        print("No expenses recorded.")


print("💰 Simple Expense Tracker")

expense_name = input("Enter expense name: ")
expense_amount = float(input("Enter amount: ₹"))

add_expense(expense_name, expense_amount)
show_expenses()