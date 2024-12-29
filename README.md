# Data Drive System

## Description

This project implements a basic data drive system similar to Google Drive. It allows users to create folders, upload files, and manage their data in a hierarchical structure. The system provides core functionalities like user authentication, CRUD (Create, Read, Update, Delete) operations for folders and files, and nested folder support.

## Key Features

*   **User Authentication:**
    *   User registration and login functionality.
    *   Secure user session management.
*   **Folder Management:**
    *   Create, read, update, and delete folders.
    *   Nested folder structures (folders within folders).
*   **File Management:**
    *   Upload, read, update, and delete files.
    *   Files are stored in a designated media directory.
*   **User Ownership:** Folders and files are owned by individual users.
*  **Data List and Detail View:** User can view all the folders and files, as well as detail information of a folder or a file.
*   **Confirmation for Delete:** Asks for user's confirmation before deleting a folder or a file.

## Technologies Used

*   **Python:** The programming language used.
*   **Django:** The web framework for building the application.
*   **Django ORM:** For database interaction.
*   **HTML, CSS, JavaScript:** For the basic structure and styling of the web pages.
*   **Bootstrap:** For UI framework to styling and layout
*   **SQLite3:** Default database for this project.
*   **Middleware:** Custom middleware for authentication

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/a-lolf/data_drive.git
    cd data_drive_system
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate    # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    
4.  **Apply migrations:**

    ```bash
    python manage.py makemigrations data_drive
    python manage.py migrate
    ```

5.  **Create a superuser account:**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7.  **Open the application:** Navigate to `http://127.0.0.1:8000/` in your web browser.


## Additional Notes

*   This is a basic implementation and lacks some features (e.g., password reset, sharing, detailed permissions).
*   For production deployment, consider using a more robust database than SQLite3, such as PostgreSQL or MySQL.
*   Always review your `settings.py` file to handle static files and media files settings before deploying to production.

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request or create an issue.
