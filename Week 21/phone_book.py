import json
import os

class Contact:
    def __init__(self, name, phone, email=None, address=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            name=data["name"],
            phone=data["phone"],
            email=data.get("email"),
            address=data.get("address")
        )

class PhoneBook:
    def __init__(self, filename="contacts.json"):
        self.contacts = []
        self.filename = filename
        self.load_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("Phone book is empty.")
            return
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"\nContact {idx}")
            print(f"Name   : {contact.name}")
            print(f"Phone  : {contact.phone}")
            print(f"Email  : {contact.email}")
            print(f"Address: {contact.address}")

    def search_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"\nFound Contact:")
                print(f"Name   : {contact.name}")
                print(f"Phone  : {contact.phone}")
                print(f"Email  : {contact.email}")
                print(f"Address: {contact.address}")
                found = True
                break
        if not found:
            print("Contact not found.")

    def delete_contact(self, name):
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
        if len(self.contacts) < original_count:
            print("Contact deleted successfully.")
            self.save_contacts()
        else:
            print("Contact not found.")

    def save_contacts(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump([c.to_dict() for c in self.contacts], f, indent=4)
        except Exception as e:
            print(f"Error saving contacts: {e}")

    def load_contacts(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.contacts = [Contact.from_dict(d) for d in data]
        except Exception as e:
            print(f"Error loading contacts: {e}")

def main():
    pb = PhoneBook()

    while True:
        print("\n📒 Phone Book Menu")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email (optional): ")
            address = input("Enter Address (optional): ")
            pb.add_contact(Contact(name, phone, email, address))

        elif choice == "2":
            pb.view_contacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            pb.search_contact(name)

        elif choice == "4":
            name = input("Enter name to delete: ")
            pb.delete_contact(name)

        elif choice == "5":
            print("Exiting phone book. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
