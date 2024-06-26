# Testing

## Index

- [PEP8 Validation](#pep8-validation)
- [Testing User Stories](#testing-user-stories)
- [Bugs](#bugs)
- [Known Bugs](#known-bugs)
- [Manual Testing](#manual-testing)

This project was built using [Code Institute Project Template](https://github.com/Code-Institute-Org/p3-template). HTML and JavaScript were provided with it. Therefore, no HTML, JavaScript, or browser compatibility tests were conducted.

## PEP8 Validation

The `run.py` and `student.py` files have been reformatted to adhere to PEP8 standards and validated using [CI Python Linter](https://pep8ci.herokuapp.com/).

- **run.py** validation results:

  <img src="assets/images/python-linter/run.png" alt="'run' validation" style="width:60%;">

- **student.py** validation results:

  <img src="assets/images/python-linter/student.png" alt="'student' validation" style="width:60%;">

## Testing User Stories

- **As a teacher, I want easy access to a classroom overview with all students listed.**
  - The Classroom submenu has been implemented and is accessible from the main menu.

    <img src="assets/images/features/classroom-menu.png" alt="classroom menu" style="width:50%;">

  - You can select a single classroom from the menu, and it will be displayed on the screen.

    <img src="assets/images/features/select-classroom.png" alt="select classroom" style="width:50%;">

- **As a teacher, I want the ability to filter children who may require additional assistance in the class.**
  - The Classroom submenu offers a menu option to display the classroom table with filtering options for children who need extra attention during classes.

    <img src="assets/images/features/classroom-menu.png" alt="classroom menu" style="width:50%;">

- **As a kitchen worker, I need access to any additional dietary requirements before preparing meals for the school.**
  - The Kitchen submenu is available, filtering all children with any dietary requirements and allergies, and displays a table for the entire school.

   <img src="assets/images/features/kitchen-menu.png" alt="kitchen menu" style="width:50%;">

- **As a teacher or medical personnel, I want to be able to filter all children in school based on specific criteria such as allergies, dietary requirements, medications, or special needs.**
  - The Classroom submenu provides filtering options for each medical section, including allergies, dietary requirements, medications, special needs, and medical notes. It also shows a full table with all these requirements for the whole school.

    <img src="assets/images/features/medical-menu.png" alt="medical menu" style="width:50%;">

- **As a teacher, I want to add a new student to the classroom.**
  - The Admin submenu includes an option to add a new student with a step-by-step interface guiding the teacher through entering each entry.

    <img src="assets/images/features/add-new-student.png" alt="add student" style="width:50%;">

- **As a teacher, I want to create a new classroom.**
  - The Admin submenu offers an option to add a new classroom, validating if a classroom with that name already exists, thus preventing duplicate classroom creations.

    <img src="assets/images/features/add-classroom.png" alt="add classroom" style="width:50%;">

- **As a teacher, I want to remove a student from the class.**
  - The Admin submenu provides an option to search for a student, returning a list of students (or multiple students if there are duplicates) and allowing the teacher to choose which student to remove.

    <img src="assets/images/features/remove-student.png" alt="remove student" style="width:50%;">

- **As a teacher, I want to remove a classroom.**
  - The Admin submenu for removing classrooms lists all classrooms already created and offers the option to select which classroom the teacher would like to remove.

    <img src="assets/images/features/remove-classroom.png" alt="remove classroom" style="width:50%;">

## Bugs

- While attempting to install the `rich` library in Gitpod, the system indicated that the library was already installed, although it was never installed previously. This issue caused problems when deploying the project to Heroku, as the project failed to run due to the `rich` library missing from the `requirements.txt` file.

  **Solution:** Manually added `rich==13.7.1` to the `requirements.txt` file.

- The "Quit" option in the main menu was actually terminating the program abruptly, causing it to stop entirely and requiring a page reload to restart. This behaviour was inconvenient for users as it interrupted their workflow. To address this issue, the "Quit" option was replaced with a system exit imitation that clears the console, displays a goodbye message, and returns the user back to the main menu seamlessly.

## Known Bugs

- There is a bug that may display artefacts from previous interactions in the upper section of the screen. This issue is not immediately visible until the user scrolls up the screen. It occurs due to the console template's limitations of a 24-character height and 80-character width. During the project planning phase, I anticipated this limitation and designed the project with scrollable content in mind. Initially, I did not encounter this problem while testing the project in Gitpod. However, after deploying the project, overflow text lines became permanently stuck in the upper part of the screen, resembling display artefacts. These artefacts may accumulate if vertical overflow continues to occur. Despite my efforts, I have not been able to resolve this issue completely.

    - To mitigate overflow, I implemented several measures. Firstly, I modified the display of tables. Previously, dietary requirements and medical tables were designed to display all tables for all classrooms simultaneously. I changed this to display only one class at a time, requiring the user to press enter to view another table. This significantly reduced the amount of scrollable content. Additionally, I limited the number of students entered per classroom to 4 or 5. While this is not a strict restriction, users can add as many students as they like. This helped further reduce the overflow effect, though it has not been completely eliminated. While not immediately visible, users may encounter overflow artefacts if they scroll up the main menu screen or tables.

## Manual Testing

**[Download Excel Testing File](/assets/testing-table/testing.xlsx)**

![Testing table](/assets/images/testing/testing.webp)