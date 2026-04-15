import os

FILENAME = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    return contacts
    
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")
            
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    save_contacts(contacts)
    print(f"{name} has been added!\n")
    
def view_contacts(contacts):
    if not contacts:
        print("No contacts saved yet.\n")
    else:
        print("\nYour Contacts:")
        for name, phone in contacts.items():
            print(f"  {name} - {phone}")
        print()
        
def delete_contact(contacts):
    name = input("Enter the name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name} has been deleted.\n")
    else:
        print("Contact not found!\n")
        
contacts = load_contacts()

print("Welcome to your Contact Book!")

while True:
    print("1. Add contact")
    print("2. View contacts")
    print("3. Delete contact")
    print("4. Quit")
    
    choice = input("\nChoose an option: ").strip()
    
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        delete_contact(contacts)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.\n")