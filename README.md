# MyClassroom: Empowering Teachers, Supporting Every Child

## Introduction

MyClassroom is a command line interface application running in Python terminal. A classroom management tool born from an understanding of the diverse needs of students and the challenges faced by teachers in addressing them. MyClassroom aims to simplify the complex task of classroom management while ensuring that every child receives the care and attention they deserve. 

With MyClassroom, teachers gain access to a simple overview of their classrooms, allowing them to track students' medical or dietary needs, preferences, and behaviors effortlessly. From dietary restrictions to social anxieties, MyClassroom empowers teachers to provide personalized support, fostering an inclusive and nurturing learning environment for all.

## Project Inception

In the heart of every classroom lies a world of diversity, where each child brings their unique needs, fears, and joys. And it happens that we are lucky to have one joyful little person, who sometimes needs a little extra attention and care. I've often wondered at the incredible dedication of teachers who tirelessly work ensuring that every child feels safe, understood, and valued.

Little joyfuls persons journey sparked my curiosity about the complexities teachers face in managing classrooms. How do they remember each child's special instructions, fears, and preferences amidst the whirlwind of daily activities? How do they maintain a nurturing environment while juggling diverse needs and personalities?

I wondered about the tools available to teachers for sharingthis important information across departments, and the strategies for seamlessly transitioning responsibilities when a teacher is absent. These reflections ignited the idea for MyClassroom – a simple software solution aimed at supporting teachers and enhancing the educational experience for every child. MyClassroom is a commitment to ensuring that every child receives the care and attention they deserve. With MyClassroom, teachers can effortlessly access a comprehensive overview of their classrooms, allowing them to track students' needs, preferences, and behaviors with ease. From dietary restrictions to social anxieties, MyClassroom empowers teachers to provide personalized support, creating an inclusive learning environment for all.

## User Stories

- As a teacher, I want easy access to a classroom overview with all students listed.
- As a teacher, I want the ability to filter children who may require additional assistance in the class.
- As a kitchen worker, I need access to any additional dietary requirements before preparing meals for the school.
- As a teacher or medical personnel, I want to be able to filter all children in school based on specific criteria such as allergies, dietary requirements, medications, or special needs.
- As a teacher, I want to add a new student to the classroom.
- As a teacher, I want to create a new classroom.
- As a teacher, I want to remove a student from the class.
- As a teacher, I want to remove a classroom.

## Flowchart

## How To Use MyClassroom 

## Features

## Data Model

## Setting Up Google API

1. Login to [Google Cloud Platform](https://cloud.google.com/)
2. Click the drop-down menu next to the "Google Cloud" logo (it may display the name of another project you are currently working on) and select "NEW PROJECT" to create a new project.
3. Enter the name of your project in the provided field on the new screen, then click "Create" to proceed.
4. After creating your project, return to the main page of Google Cloud Platform. Select the project you just created from the drop-down menu next to the "Google Cloud" logo.
5. In the "Quick Access" menu, click on "APIs & Services".
6. In the new window, select the "Libraries" option from the menu on the left side of your screen.
7. In the "API library" window, use the search bar to find "Google Drive API".
8. From the search results, select "Google Drive API" and click the "ENABLE" button.
9. A new window titled "Enabled APIs and services" will open. To grant permission for your Python project to access Google Drive, you will need to generate credentials.
10. Click on the "CREATE CREDENTIALS" button.
11. In the "Credential Type" window:
    1. In the "Which API are you using?" section, select "Google Drive API" from the drop-down menu.
    2. In the "What data will you be accessing?" section, select "Application Data", then click "Next".
12. In the "Service account details" section, enter a name for your service account, then click "CREATE AND CONTINUE".
13. In the "Grant this service account access to the project" section, select **Basic > Editor** from the "Select a role" drop-down menu, then click "Continue".
14. Leave the options in the "Grant users access to this service account (optional)" section blank, then click "DONE".
15. You will be taken back to the "APIs and services" screen. Select the "Credentials" option from the menu on the left side of the screen.
16. Click on your newly created service account in the "Service accounts" section, then select the "KEYS" tab.
17. In the "ADD KEY" drop-down menu, select "Create New Key".
18. Choose "JSON" as the key type, then click "Create".
19. This will download a JSON file containing your API credentials to your computer.
20. Return to the "API Library" and search for "Google Sheets API".
21. Select "Google Sheets API" from the search results, then click "ENABLE" to enable it.

## Setting Up the Development Environment

1. Locate the JSON file containing your Google API credentials on your computer. Drag and drop it into your workspace, then rename it to "creds.json".
2. Open the "creds.json" file and locate the "client_email" key value. Copy this value.
3. Navigate to your Google Sheets, open the desired spreadsheet, and click the "Share" button in the top right corner.
4. Paste the "client_email" key value from the "creds.json" file into the sharing settings.
5. Ensure that the "Editor" permission is selected. Uncheck the "Notify people" option, then click the "Share" button.
6. Return to your workspace and open the ".gitignore" file, which contains a list of files that should not be committed to GitHub.
7. Add "creds.json" to the list of ignored files in the ".gitignore" file.

## Connecting to API with Python

1. Open your IDE and install the google-auth and gspread libraries:
    In the terminal window, type `pip3 install gspread google-auth` and press Enter.
2. Open your Python file.
3. Import dependencies into your Python file using:
    ```python
    import gspread
    from google.oauth2.service_account import Credentials
    ```
4. Set the scope below:
    ```python
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    ```
5. Create a constant variable `CREDS`, passing the `creds.json` file we added earlier:
    ```python
    CREDS = Credentials.from_service_account_file('creds.json')
    ```
6. Create another variable named `SCOPED_CREDS`, passing the `SCOPE` variable:
    ```python
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    ```
7. Create a gspread client using the `gspread.authorize` method and passing the `SCOPED_CREDS` variable:
    ```python
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    ```
8. Finally, create a constant variable `SHEET`, passing the name of our spreadsheet:
    ```python
    SHEET = GSPREAD_CLIENT.open('my_classroom')
    ```
## Deploying Project to Heroku

1. In your workspace, add dependencies to the `requirements.txt` file for Heroku to install these dependencies and be able to run them. In the IDE terminal, run this code:
    ```
    pip3 freeze > requirements.txt
    ```
    Then push the changes to your GitHub repository.
2. Log in to [Heroku](https://heroku.com/).
3. In the Heroku dashboard, click the "Create new app" button.
4. In the "Create New App" section, enter the app name, select your region from the dropdown list, and click the "Create app" button.
5. In your app's dashboard, go to the settings tab and locate the "Config Vars" section.
6. Click the "Reveal Config Vars" button.
7. In the "KEY" field, enter "CREDS".
8. Go back to your workspace, copy the entire content of the "creds.json" file.
9. Return to the Heroku "Config Vars" section, paste the content of "creds.json" into the "VALUE" field, and click the "Add" button.
10. In the "Config Vars" section, add an additional "KEY"  ```PORT``` with the value of ```8000``` and press the "Add" button.
11. Now scroll down to the "Buildpacks" section and click the "Add buildpack" button.
12. Select the "python" buildpack and click the "Save changes" button.
13. In the "Buildpacks" section, click the "Add buildpacks" button again, this time select "nodejs" and click the "Save changes" button.
14. Ensure that buildpacks are stacked in this order: "heroku/python" on top and "heroku/nodejs" below it.
15. In your app's dashboard, go to the "Deploy" section.
16. In the "Deployment method" section, select "GitHub" and press the "Connect to GitHub" button.
17. The "Search for a repository" search bar will be displayed. Enter your GitHub repository name and press the "Search" button.
18. This should display your repository below the search bar, click the "Connect" button.
19. Scroll down to the "Automatic deploys" section and press "Enable Automatic Deploys". This will allow Heroku to rebuild your app every time you push changes to your GitHub repository. If you prefer to deploy it manually, you can leave this option disabled and use the "Deploy Branch" button in the "Manual deploy" section to deploy your app manually.
20. A "Your app was successfully deployed." message will be displayed, along with a button linking to the deployed app.

## Technologies Used

- [Project template](https://github.com/Code-Institute-Org/p3-template) provided by Code Institute consisting of:
    - HTML
    - JavaScript

- [Python](https://www.python.org/): Main language used to build the application.

- [GitHub](https://github.com/): Used for pushing and storing application code.

- [GitPod](https://www.gitpod.io/): Cloud development environment used to develop the application.

- [Google Cloud](https://cloud.google.com/): Used API feature to connect Google Sheets with the application.

- [Google Sheets](https://www.google.com/sheets/about/): Used to store and manipulate application data.

- [Heroku](https://www.heroku.com): Used to deploy the application.

- [Lucidchart](https://www.lucidchart.com/pages/): Used to create flowchart for the project.

## Python Libraries

## Testing 

## Credits