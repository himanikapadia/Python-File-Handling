FILENAME = "expenses.txt"


def add_expense(name, amount):
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{name},{amount:.2f}\n")


def show_expenses():
    print("\n------------------------------")
    print("       YOUR EXPENSES")
    print("------------------------------")

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses recorded.")
            return

        total = 0.0

        for line in expenses:
            if "," in line:
                name, amount_str = line.strip().split(",")
                amount = float(amount_str)
                # Neat columns: 18 spaces for name, right-aligned amount
                print(f"- {name:<18} ₹{amount:>8.2f}")
                total += amount

        print("------------------------------")
        print(f"  {'Total':<18} ₹{total:>8.2f}")
        print("------------------------------")

    except FileNotFoundError:
        print("No expenses recorded.")


# --- Main Program ---
print("==============================")
print("    Simple Expense Tracker")
print("==============================")

name = input("Enter expense name: ").strip()

try:
    amount = float(input("Enter amount: ₹"))
    if name and amount > 0:
        add_expense(name, amount)
        show_expenses()
    else:
        print("Please enter a valid name and an amount greater than 0.")
except ValueError:
    print("Invalid amount! Please enter numbers only.")