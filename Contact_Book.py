def add_contact(name1, phone1, email1, address1):
    """Adds a new contact to the contact book."""
    contacts.append({
        "Name": name1,
        "phone": phone1,
        "email": email1,
        "address": address1
    })


def edit_contact(new_name, new_phone_num, new_email_address, new_address_num):
    """Edits an existing contact in the contact book."""
    for contact in contacts:
        if contact["name"] == new_name:
            contact["phone"] = new_phone_num
            contact["email"] = new_email_address
            contact["address"] = new_address_num
            break


def delete_contact(del_name):
    """Deletes a contact from the contact book."""
    for contact in contacts:
        if contact["name"] == del_name:
            contacts.remove(contact)
            break


def list_contacts():
    """Lists all contacts in the contact book."""
    for contact in contacts:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Address:", contact["address"])


contacts = []

while True:
    print("What would you like to do?")
    print("1. Add a contact")
    print("2. Edit a contact")
    print("3. Delete a contact")
    print("4. List contacts")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the contact name: ")
        phone = input("Enter the contact phone number: ")
        email = input("Enter the contact email address: ")
        address = input("Enter the contact address: ")
        add_contact(name, phone, email, address)

    elif choice == "2":
        name = input("Enter the contact name to edit: ")
        new_phone = input("Enter the new phone number: ")
        new_email = input("Enter the new email address: ")
        new_address = input("Enter the new address: ")
        edit_contact(name, new_phone, new_email, new_address)

    elif choice == "3":
        name = input("Enter the contact name to delete: ")
        delete_contact(name)

    elif choice == "4":
        list_contacts()

    elif choice == "5":
        break
