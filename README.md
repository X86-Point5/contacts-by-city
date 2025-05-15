# Contact Book Application (ContactsByCity)

**Author:** Maximus Barraza (Github: X86-Point5)
**Version:** 1.0.0 (app.py), 1.0.0 (FileOperator.py), 1.1.0 (InputHandler.py)
**Date:** May 15, 2025
**Development Environment:** Windows

## Purpose

This project is a console-based Contact Book application developed in Python. It serves as a documentation of progress in developing a functional application with features like data persistence using CSV files, modular code structure, and user input handling.

This application is intended as a documentation of progress and is specifically designed for a Windows environment.

## Features

* **Contact Management:**
    * Add new contacts with first name, last name, city, and email.
    * Prevents duplicate contacts based on email addresses.
    * Remove existing contacts by their email address.
* **Data Persistence:**
    * Contacts are loaded from and saved to a `contacts.csv` file.
    * Includes a basic integrity check for the `contacts.csv` file upon loading.
* **Contact Viewing & Filtering:**
    * Display all stored contacts.
    * Filter contacts by city.
* **User-Friendly Console Interface:**
    * Menu-driven navigation.
    * Clear screen functionality for better readability (Windows specific).
    * Pause prompts for user acknowledgment (Windows specific).

## Project Structure

The project consists of the following key files:

* `app.py`: The main application file that orchestrates the contact book logic and user interface.
* `FileOperator.py`: A utility module providing functions for file and directory operations, including CSV handling.
* `InputHandler.py`: A utility module providing functions for robust user input validation from the console.
* `contacts.csv`: The CSV file used to store and retrieve contact data.

## Dependencies & Setup

This application relies on the following components being present in the same directory as `app.py`:

1.  **`InputHandler.py`**: Custom module for input validation.
2.  **`FileOperator.py`**: Custom module for file operations.
3.  **`contacts.csv`**: Data file for storing contacts.
    * The CSV file must exist and, if not empty, should have the following header row: `FirstName,LastName,City,Email`
    * If `contacts.csv` is missing or malformed (e.g., missing headers, inconsistent column lengths), the application will display an error and exit. A sample `contacts.csv` might look like this:
        ```csv
        FirstName,LastName,City,Email
        John,Doe,New York,john.doe@example.com
        Jane,Smith,Los Angeles,jane.smith@example.com
        ```

## How to Run

1.  Ensure you have Python 3 installed on your Windows system.
2.  Place `app.py`, `FileOperator.py`, `InputHandler.py`, and `contacts.csv` in the same directory. Let's assume this directory is named `ContactBookProject`.
3.  Open a command prompt or PowerShell.
4.  Navigate to the project directory using the `cd` command:
    ```bash
    cd path\to\your\ContactBookProject
    ```
    (Replace `path\to\your\ContactBookProject` with the actual path to the directory).
5.  Run the application using the command:
    ```bash
    py app.py
    ```
    (Or `python app.py` if `py` is not aliased to your Python 3 interpreter).
6.  Follow the on-screen menu prompts to manage your contacts.

## Windows Specificity

This application uses Windows-specific commands for clearing the console (`cls`) and pausing execution (`pause`). This is intentional as the project is documented as being developed and tested primarily on a Windows environment for the purpose of documenting progress within that context.

## License

This work is dedicated to the public domain. You are free to use, modify, and distribute it as you see fit.

---
