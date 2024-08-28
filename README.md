# Contact-Management-System

## Overview

The Contact Management System is a Python-based command-line application designed to manage a user's contact details efficiently. The application provides a range of functionalities from adding new contacts to searching, updating, and deleting existing contacts.

## Features

Contact Creation

- create_contact Function: Constructs a new contact dictionary from the provided name, number, and email. Each contact's details are encapsulated in this dictionary, which is then ready to be added to the main contact list.

Contact Addition

- add_contact Function: Adds the newly created contact dictionary to the central contacts dictionary, with the contact's name as the key and their details (number and email) as the value. This method ensures that each contact is uniquely identifiable by their name.

Contact Search

- find_contact Function: Searches the entire contacts dictionary for a contact matching the given search term (name, number, or email). If found, it returns a dictionary containing the contact's details, otherwise returns None.

Contact Deletion

- delete_contact Function: Removes a contact from the dictionary based on a provided search term that can match the contact's name, number, or email. If the contact is found and successfully deleted, it confirms the deletion; if not, it reports that the contact was not found.

Contact Update

- update_contact Function: Modifies an existing contact's details based on the provided search term. If the contact is found, it allows updating the contact's name, number, and/or email. If no contact is found, it adds a new contact with the provided details.

Display All Contacts

- display_contacts Function: Lists all the contacts stored in the dictionary, displaying each contact's name, number, and email. If no contacts are stored, it indicates that there are no contacts available.

User Interface Management

- main_menu Function: Provides a simple text-based menu system that prompts the user to choose from adding, searching, updating, deleting, or displaying contacts, or exiting the application.

- user_interface Function: Manages the application's flow, responding to user input based on the choice made at the main menu and calling the appropriate function to handle the user's request.

System Architecture

- The system is structured around a central dictionary (contacts), where all contact information is stored. Each function interacts with this dictionary, performing specific operations as required. This modular approach not only keeps the code clean and manageable but also enhances maintainability and scalability.

![image](https://github.com/user-attachments/assets/5c3b79d7-cf08-400f-b858-1485bd5cdcbc)
