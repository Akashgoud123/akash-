
contacts = []

def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contact = {"name": name, "phone_number": phone_number, "email": email, "address": address}
    contacts.append(contact)
    print(f"Contact '{name}' added!")

def view_contact_list():
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone_number']}")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact["name"] or search_term in contact["phone_number"]]
    if found_contacts:
        print("\nSearch Results:")
        for i, contact in enumerate(found_contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone_number']}")
    else:
        print("No contacts found!")

def update_contact():
    view_contact_list()
    contact_num = int(input("Enter the contact number to update: ")) - 1
    if contact_num < len(contacts):
        contact = contacts[contact_num]
        print(f"Updating contact '{contact['name']}'...")
        contact["name"] = input("Enter the new name: ")
        contact["phone_number"] = input("Enter the new phone number: ")
        contact["email"] = input("Enter the new email: ")
        contact["address"] = input("Enter the new address: ")
        print(f"Contact '{contact['name']}' updated!")
    else:
        print("Invalid contact number!")

def delete_contact():
    view_contact_list()
    contact_num = int(input("Enter the contact number to delete: ")) - 1
    if contact_num < len(contacts):
        del contacts[contact_num]
        print("Contact deleted!")
    else:
        print("Invalid contact number!")

def main():
    while True:
        print("\nContact Information Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
