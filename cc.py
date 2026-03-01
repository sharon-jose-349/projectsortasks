import os

# File name
filename = "contacts.txt"

# Ensure file exists
if not os.path.exists(filename):
    with open(filename, "w") as f:
        pass  # just create empty file


# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    with open(filename, "a") as f:
        f.write(f"{name},{phone}\n")

    print(f"Contact {name} added successfully!\n")


# Function to show all contacts
def show_contacts():
    print("\n--- All Contacts ---")
    with open(filename, "r") as f:
        for line in f:
            name, phone = line.strip().split(",")
            print(f"Name: {name}, Phone: {phone}")
    print("-------------------\n")


while True:
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")