"""
This module provides functionality for managing
student information in MyClassroom.
"""

# Third-party imports
import gspread  # Google Sheets API library
from google.oauth2.service_account import Credentials  # Google credentials

# Google Sheets authentication
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Loading credentials from the JSON file
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Opening the Google Sheets document named 'my_classroom'
SHEET = GSPREAD_CLIENT.open("my_classroom")


class Student:
    """Represents a student in MyClassroom."""

    sid = SHEET.worksheet(
        "sid"
    )  # Get the sid worksheet containing the student ID to iterate over

    def __init__(
        self,
        name: str,
        allergies="",
        dietary="",
        medication="",
        special_needs="",
        notes="",
    ):
        """
        Initialize a new student.

        Args:
            name (str): The name of the student.
            allergies (str, optional): Any allergies the student has.
                Defaults value "".
            dietary (str, optional): Dietary restrictions of the student.
                Defaults value "".
            medication (str, optional): Medications taken by the student.
                Defaults value "".
            special_needs (str, optional): Special needs of the student.
                Defaults value "".
            notes (str, optional): Additional notes about the student.
                Defaults value "".
        """
        self.name = name
        self.allergies = allergies
        self.dietary = dietary
        self.medication = medication
        self.special_needs = special_needs
        self.notes = notes

        # Assign student id to worksheets A1 cell value
        self.id = int(Student.sid.acell("A1").value)
        # Increment ID value by one for each new student
        cell_value = int(Student.sid.acell('A1').value)
        Student.sid.update_acell("A1", f"{cell_value + 1}")

    def add_student(self, worksheet_name: str):
        """
        Adds a new student to the specified classroom worksheet.

        Args:
            worksheet_name (str): The name of the class worksheet.
        """
        class_name = SHEET.worksheet(worksheet_name.upper())
        worksheet_len = len(class_name.col_values(2)) + 1
        # Update cells with student information
        class_name.update_cell(
            worksheet_len, 1, f"{int(Student.sid.acell('A1').value) + 1}"
        )
        class_name.update_cell(worksheet_len, 2, self.name.title())
        class_name.update_cell(worksheet_len, 3, self.allergies.capitalize())
        class_name.update_cell(worksheet_len, 4, self.dietary.capitalize())
        class_name.update_cell(worksheet_len, 5, self.medication.capitalize())
        class_name.update_cell(
            worksheet_len, 6, self.special_needs.capitalize()
        )
        class_name.update_cell(worksheet_len, 7, self.notes.capitalize())

    @staticmethod
    def delete_student(classroom_name: str, row_id: int):
        """
        Deletes a student from the classroom.

        Args:
            classroom_name (str): The name of the class worksheet.
            row_id (int): The row index of the student to delete.
        """
        worksheet = SHEET.worksheet(classroom_name.upper())
        try:
            worksheet.delete_rows(row_id)
        except Exception as e:
            print(
                f"Error occurred while deleting row {row_id}"
                f" in worksheet {classroom_name.upper()}: {e}"
            )
            pass
