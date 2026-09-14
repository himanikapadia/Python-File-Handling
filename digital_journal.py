from datetime import datetime

FILENAME = "journal.txt"


def write_entry():
    print("\n--- Write Today's Entry ---")
    data = input("~ Start Writing ~\n").strip()

    if not data:
        print("Empty entry skipped. Nothing was saved.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_entry = f"[{timestamp}]\n{data}\n{'-' * 30}\n"

    try:
        with open(FILENAME, "a", encoding="utf-8") as file:
            file.write(formatted_entry)
        print("Saved successfully!")
    except OSError as e:
        print(f"Error saving entry: {e}")


def read_entries():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if content:
                print("\n===== Your Journal =====")
                print(content)
            else:
                print("\nYour journal file is currently empty.")
    except FileNotFoundError:
        print("\nNo journal entries found yet.")
    except OSError as e:
        print(f"\nError reading journal: {e}")


def main():
    print("====== Welcome to Digi-Journal =====")
    write_entry()

    choice = input("\nDo you want to read all journal entries? (yes/no): ").strip().lower()
    if choice in ("yes", "y"):
        read_entries()
    elif choice in ("no", "n"):
        print("Thank you for using Digi-Journal!")
    else:
        print("Invalid choice, exiting.")


if __name__ == "__main__":
    main()