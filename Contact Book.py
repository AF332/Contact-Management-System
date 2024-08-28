"""Creating a dictionary to contain the name, number, and email of a new contact."""
def create_contact(name, number, email):
    return {
        'name': name,
        'number': number,
        'email': email
    }

"""Creating a larger contacts list dictionary called 'contacts'. The name of the new contact created is used as the key in the larger contacts list 'contacts' and the number and email of the new contact is stored as the values of the dictionary."""
def add_contact(contacts, contact):
    contacts[contact['name']] = {
        'number': contact['number'],
        'email': contact['email']
    }

"""Function that loops over the 'contacts' dictionary items. If the search term matches any of the dictionaries items (name, number, email) the found contact dictionary is return. If contact not found then 'None' is returned."""
def find_contact(contacts, search_term):
    for name, details in contacts.items():
        if search_term in [name, details['number'], details['email']]:
            return {name: details}
    return None

"""Function to remove a contact from a dictionary based in a search term. Can either be name, number or email."""
def delete_contact(contacts, search_term):
    found_name = None # Initialised and later used to store the name of the contact that matches the search term if such contact is found.
    for name, details in contacts.items(): # Loops through all the contacts items.
        if search_term in [name, details['number'], details['email']]: # This line checks if the search_term matches any of the following: the contact's name (name), the contact's phone number (details['number']), or the contact's email (details['email']).
            found_name = name # Stores found name and exit loops.
            break
    
    if found_name:
        contacts.pop(found_name) # Delete the contact.
        return f"Contact '{found_name}' deleted successfully."
    else:
        return "Contact not found!"

"""Function to modify an existing contact's details on a contacts dictionary based on a provided search term, or add a new contact if no match is found using the search term."""
def update_contact(contacts, search_term, new_name=None, new_number=None, new_email=None):
    
    result = find_contact(contacts, search_term) # Find the contact using the search term.

    if result: # Checks if the contact was found.
        old_name = next(iter(result)) # Gets the first key from the dictionary of the contact.
        details = result[old_name] # Access the contact details like the number and email.

        updated_details = {
            'number': new_number or details['number'],
            'email': new_email or details['email']
        } # Creates a new dictionary that contains the updated contact details. It uses the new values provided (if any) or defaults to the existing values.

        if new_name and new_name != old_name: # Checks if the new name has been provided and if it differs from the old name.
            contacts[new_name] = updated_details # If renaming is necessary, this line assigns the updated_details to the new_name in the contacts dictionary.
            contacts.pop(old_name) # Properly delete the old entry after transferring the details.
            return f"Contact '{old_name}' changed to '{new_name}' and updated successfully."
        else:
            contacts[old_name] = updated_details  # Update the existing entry without renaming.
            return f"Contact '{old_name}' updated successfully."
    
    else:
        # If contact does not exist, use add_contact to add it.
        new_contact = create_contact(search_term, new_number, new_email)
        add_contact(contacts, new_contact)

        return f"New contact '{search_term}' added successfully!"

"""Function handles the main options of the application."""
def main_menu():
    print("\nWelcome to the Contact Management System")
    print("1. Add a New Contact")
    print("2. Find a Contact")
    print("3. Update an Existing Contact")
    print("4. Delete a Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

"""Function takes 'contacts' dictionary as an argument and displays all contacts."""
def display_contacts(contacts):
    if not contacts: # checks if the dictionary is empty.
        print("No contacts available.")
    else: # If not empty
        for name, details in contacts.items(): # Iterates over each item in the contacts dictionary and prints the name, number, and email of each contact.
            print(f"Name: {name}, Number: {details['number']}, Email: {details['email']}") 

"""Function orchestrates the application flow."""
def user_interface():
    contacts = {}
    while True: # Starts infinite loop.
        choice = main_menu()
        if choice == '1': # Option to add a new contact.
            name = input("Enter the contact's name: ")
            number = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email address: ")
            contact = create_contact(name, number, email)
            add_contact(contacts, contact)
            print("Contact added successfully.")

        elif choice == '2': # Option to find contact.
            search_term = input("Enter the name, number, or email of the contact to find: ")
            result = find_contact(contacts, search_term)
            if result:
                for key, value in result.items():
                    print(f"Found: Name: {key}, Number: {value['number']}, Email: {value['email']}")
            else:
                print("Contact not found.")

        elif choice == '3': # Option to update contact.
            search_term = input("Enter the name, number, or email of the contact to update: ")
            new_name = input("Enter the new name (press enter to skip): ")
            new_number = input("Enter the new number (press enter to skip): ")
            new_email = input("Enter the new email (press enter to skip): ")
            print(update_contact(contacts, search_term, new_name, new_number, new_email))

        elif choice == '4': # Option to delete contact.
            search_term = input("Enter the name, number, or email of the contact to delete: ")
            print(delete_contact(contacts, search_term))

        elif choice == '5': # Option to display all contacts.
            display_contacts(contacts)

        elif choice == '6': # Option to exit application.
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice, please try again.") # Handles invalid inputs.

"""Calls the user_interfact function to run the script."""
if __name__ == "__main__":
    user_interface()