FILENAME = "students.txt"


def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(FILENAME, "a") as file:
        file.write(f"{name},{marks}\n")

    print("Student record added!")


def show_students():
    try:
        with open(FILENAME, "r") as file:
            students = file.readlines()

        if not students:
            print("No student records found.")
            return

        print("\nSTUDENT RECORDS")
        print("-" * 35)

        for index, student in enumerate(students, start=1):
            name, marks = student.strip().split(",")
            print(f"{index}. {name} - Marks: {marks}")

    except FileNotFoundError:
        print("No student records found.")


def search_student():
    search_name = input("Enter student name: ").lower()

    try:
        with open(FILENAME, "r") as file:
            students = file.readlines()

        found = False

        for student in students:
            name, marks = student.strip().split(",")

            if search_name in name.lower():
                print(f"Found: {name} - Marks: {marks}")
                found = True

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


def main():
    while True:
        print("\nSTUDENT RECORD MANAGER")
        print("=" * 35)
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Exit")
        print("=" * 35)

        choice = input("Enter your choice: ")

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
            print("Invalid choice. Try again.")


main()