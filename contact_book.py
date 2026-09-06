# contact_book.py

def add_contact(name, phone):
    with open("contacts.txt", "a") as file:
        file.write(f"{name}: {phone}\n")
    print(f"Saved {name}!")

def show_contacts():
    try:
        with open("contacts.txt", "r") as file:
            print("\n--- Contacts List ---")
            print(file.read().strip())
    except FileNotFoundError:
        print("No contacts found yet.")

# Quick demonstration
add_contact("Aarav", "9876543210")
add_contact("Priya", "9123456780")
show_contacts()