def add_contact(name, phone, email, address):
  """Adds a new contact to the contact book."""
  contacts.append({
      "name": name,
      "phone": phone,
      "email": email,
      "address": address
  })

def edit_contact(name, new_phone, new_email, new_address):
  """Edits an existing contact in the contact book."""
  for contact in contacts:
    if contact["name"] == name:
      contact["phone"] = new_phone
      contact["email"] = new_email
      contact["address"] = new_address
      break

def delete_contact(name):
  """Deletes a contact from the contact book."""
  for contact in contacts:
    if contact["name"] == name:
      contacts.remove(contact)
      break

def list_contacts():
  """Lists all contacts in the contact book."""
  for contact in contacts:
    print(contact)

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

  else:
    print("Invalid choice.")