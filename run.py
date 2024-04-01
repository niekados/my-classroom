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