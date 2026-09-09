def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")

    print("Contact added successfully!")


def show_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("📭 No contacts found.")
            return

        print("\nCONTACTS")
        print("-" * 30)

        for index, contact in enumerate(contacts, start=1):
            name, phone = contact.strip().split(",")
            print(f"{index}. {name} - {phone}")

    except FileNotFoundError:
        print("No contacts found.")


def search_contact():
    search = input("Enter name to search: ").lower()

    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        found = False

        for contact in contacts:
            name, phone = contact.strip().split(",")

            if search in name.lower():
                print(f"Found: {name} - {phone}")
                found = True

        if not found:
            print("Contact not found.")

    except FileNotFoundError:
        print("No contacts found.")


def main():
    while True:
        print("\nCONTACT MANAGER")
        print("=" * 30)
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Search Contact")
        print("4. Exit")
        print("=" * 30)

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()