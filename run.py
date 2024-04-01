import gspread
from google.oauth2.service_account import Credentials
import os
import re

# Google Sheets authentication
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Loading credentials from the JSON file
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Opening the Google Sheets document named 'my_classroom'
SHEET = GSPREAD_CLIENT.open('my_classroom')

def press_enter_to_continue():
    """
    Prompts the user to press Enter to return to the main menu.
    """
    input("\nPress Enter to return to the main menu...\n")

def show_menu(menu_options, menu_title):
    """
    Displays a menu with options and a title.

    Args:
        menu_options (list): List of options to display in the menu.
        menu_title (str): Title of the menu.
    """
    # Clear the console
    clear_console()

    # Display the appropriate logo based on the menu title
    if menu_title == "Main Menu":
        my_class_logo()
    else:
        mini_logo()

    # Print the title of the menu
    print_menu_title(menu_title)

    # Print each option in the menu
    for option in menu_options:
        print(f"{menu_options.index(option) + 1}. {option}")

    # Print the quit option if it's the main menu, otherwise print the option to return to the main menu
    if menu_title == "Main Menu":
        print(f"{len(menu_options) + 1}. Quit\n")
    else:
        print(f"{len(menu_options) + 1}. Back to Main Menu\n")


def get_valid_choice(menu_options):
    """
    Get a valid menu choice from the user.

    Args:
        menu_options (list): List of menu options.

    Returns:
        int: Valid menu choice.
    """
    while True:
        try:
            # Prompt the user to enter a choice
            print(f"Type a number between 1 and {len(menu_options) + 1}.")
            choice = int(input("Enter your choice: "))
            
            # Check if the choice is within the valid range
            if 1 <= choice <= len(menu_options) + 1:
                return choice
            else:
                # Print error message for invalid choice
                print(f"Invalid choice. Please enter a number between 1 and {len(menu_options) + 1}.")
        
        except ValueError:
            # Print error message for invalid input (non-integer)
            print("Invalid input. Please enter a number.")

def kitchen_menu():
    """
    Displays a menu for selecting kitchen options and performs corresponding actions.

    Options:
    1. Dietary Requirements (Displays students with dietary information)
    """
    menu_title = "Kitchen Menu"
    kitchen_options = ["Dietary Requirements"]
    
    # Display the menu options
    show_menu(kitchen_options, menu_title)
    
    # Get the user's choice
    choice = get_valid_choice(kitchen_options)
    
    if choice == len(kitchen_options) + 1:
        return  # Quit
    elif choice == 1:
        clear_console()
        print_menu_title("Dietary Requirements")
        # Display students' dietary requirements
        filter_all_worksheets("name", "dietary", "allergies", check_empty_med_cells=True)
        press_enter_to_continue()  # Wait for user to press Enter before returning to main menu

def medical_menu():
    """
    Displays a menu for selecting medical options and performs corresponding actions.

    Options:
    1. Allergies (Displays students with allergies)
    2. Dietary Requirements (Displays students with dietary requirements)
    3. Medication (Displays students with medication information)
    4. Special Needs (Displays students with special needs)
    5. Notes (Displays students' medical notes)
    6. All (Displays students with all medical information)
    """
    menu_title = "Medical Menu"
    medical_options = ["Allergies", "Dietary", "Medication", "Special Needs", "Notes", "All"]
    
    # Display the menu options
    show_menu(medical_options, menu_title)
    
    # Get the user's choice
    choice = get_valid_choice(medical_options)
    
    if choice == len(medical_options) + 1:
        return  # Quit
    elif 1 <= choice <= len(medical_options):
        selected_option = medical_options[choice - 1]
        clear_console()
        print_menu_title(selected_option)
        
        # Filter worksheets based on the selected medical option
        if choice == 6:
            # For option 'All', display all medical information
            filter_all_worksheets("name", "allergies", "dietary", "medication", "special needs", "notes", check_empty_med_cells=True)
        else:
            # For individual medical options, display respective information
            filter_all_worksheets("name", selected_option.lower(), check_empty_med_cells=True)
        
        press_enter_to_continue()  # Wait for user to press Enter before returning to main menu

def admin_menu():
    """
    Displays a menu for administrative tasks and performs the corresponding actions.

    Options:
    1. Add Student
    2. Add Classroom
    3. Remove Student
    4. Remove Classroom
    """
    # Display the admin menu options
    menu_title = "Admin Menu"
    admin_options = ["Add Student", "Add Classroom", "Remove Student", "Remove Classroom"]
    show_menu(admin_options, menu_title)
    
    # Get the user's choice
    choice = get_valid_choice(admin_options)
    
    # Perform actions based on user's choice
    if choice == len(admin_options) + 1:
        return  # Quit
    elif 1 <= choice <= len(admin_options):
        print(f"You chose {admin_options[choice - 1]}")
        if choice == 1:
            add_new_student_menu()  # Add a new student
        elif choice == 2:
            add_new_classroom()  # Add a new classroom
        elif choice == 3:
            remove_student()  # Remove a student
        elif choice == 4:
            remove_classroom()  # Remove a classroom

def main():
    """
    Displays the main menu and executes the selected option.

    The main menu allows the user to navigate to different sections of the program, including Classroom, Kitchen, Medical, and Admin.
    """
    while True:
        # Display the main menu options
        menu_title = "Main Menu"
        main_options = ["Classroom", "Kitchen", "Medical", "Admin"]
        show_menu(main_options, menu_title)
        
        # Get the user's choice
        choice = get_valid_choice(main_options)
        
        # Perform actions based on user's choice
        if choice == len(main_options) + 1:
            print("Goodbye!")
            break  # Quit
        elif choice == 1:
            classroom_menu()  # Navigate to Classroom menu
        elif choice == 2:
            kitchen_menu()  # Navigate to Kitchen menu
        elif choice == 3:
            medical_menu()  # Navigate to Medical menu
        elif choice == 4:
            admin_menu()  # Navigate to Admin menu

main()