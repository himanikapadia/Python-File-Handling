FILENAME = "students.txt"


def read_all_students():
    """Helper to read records safely and avoid repetitive file-handling."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            records = []
            for line in file:
                line = line.strip()
                if "," in line:
                    name, marks = line.split(",", 1)
                    records.append((name.strip(), marks.strip()))
            return records
    except FileNotFoundError:
        return []


def add_student():
    name = input("Enter student name: ").strip()
    if not name or "," in name:
        print("Error: Name cannot be empty or contain commas.")
        return

    marks = input("Enter marks (0-100): ").strip()
    if not marks.isdigit() or not (0 <= int(marks) <= 100):
        print("Error: Please enter a valid whole number between 0 and 100.")
        return

    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{name},{marks}\n")

    print(f"Record for '{name}' added successfully!")


def show_students():
    students = read_all_students()

    if not students:
        print("No student records found.")
        return

    print("\n" + "=" * 35)
    print(f"{'#':<4} {'Name':<20} {'Marks':>8}")
    print("-" * 35)
    for index, (name, marks) in enumerate(students, start=1):
        print(f"{index:<4} {name:<20} {marks:>8}")
    print("=" * 35)


def search_student():
    query = input("Enter student name to search: ").strip().lower()
    if not query:
        print("Search term cannot be blank.")
        return

    students = read_all_students()
    if not students:
        print("No student records found.")
        return

    matches = [(name, marks) for name, marks in students if query in name.lower()]

    if matches:
        print(f"\nFound {len(matches)} match(es):")
        for name, marks in matches:
            print(f"- {name:<20} : {marks} marks")
    else:
        print("No matching student found.")


def main():
    while True:
        print("\nSTUDENT RECORD MANAGER")
        print("=" * 30)
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Exit")
        print("=" * 30)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()