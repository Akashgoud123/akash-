class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully!")

    def view_contacts(self):
        if self.contacts:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name} | Phone: {contact.phone_number}")
        else:
            print("No contacts yet!")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
        if found_contacts:
            print("\nSearch Results:")
            for contact in found_contacts:
                print(f"Name: {contact.name} | Phone: {contact.phone_number}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_phone_number):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone_number = new_phone_number
                print(f"Contact '{contact.name}' updated successfully!")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' deleted successfully!")
                return
        print(f"Contact '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter search term (name or phone number): ")
            contact_manager.search_contact(search_term)
        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            contact_manager.update_contact(name, new_phone_number)
        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
