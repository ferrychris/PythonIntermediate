CLI Todo App

A simple and interactive Command Line Interface (CLI) application to manage your daily tasks. Built using Python, SQLite for database storage, and Questionary for elegant, interactive terminal menus.

Features

- Add Tasks: Quickly add new tasks with a description, status, and a target date.
- View Tasks: See a list of all your current tasks and their details.
- Update Tasks: Update the status of existing tasks.
- Delete Tasks: Remove tasks from your list.

Project Structure

- app.py: The main entry point. Handles the interactive user menu using Questionary.
- add_task.py: Prompts for task details and inserts them into the database.
- view_task.py: Fetches and displays all tasks.
- update_task.py: Prompts the user to update a specific task's status.
- delete_task.py: Removes a selected task from the database.
- todo.db: The SQLite database file (created automatically).

Requirements

- Python 3.x
- questionary package

Installation

1. Clone or download this project to your local machine.
2. Install the required dependencies using pip:
   pip install questionary

Usage
Navigate to the project folder in your terminal and run the main application script:
python app.py

Use your arrow keys to navigate the interactive menu and press Enter to select an action.

Database Schema
Tasks are stored in a SQLite database (todo.db) with the following fields:

- id (INTEGER, Primary Key)
- task_description (TEXT)
- task_status (TEXT)
- task_todo_date (TEXT)
- task_created_date (DATE, Defaults to current date)
- task_updated_date (DATE, Defaults to current date)

Learning-
Python OOP

Problems
Hard to Test, Debug Reuse And Too Large to Maintian
Good OOP Archite
Handles Errors and Modules Seperately Making it Easy To manage

Hence Every Class Handles Only One task and One method so it is Easy to manage and test.
Every class has one job.

This follows the Single Responsibility Principle (SRP).
Instead of:

public function checkout()
{
#500 lines of code
}

We Fetch From Another Module or class

public function checkout(Request $request)
{
    return $this->orderService->checkout($request);
}
The OOP Principles

1. Encapsulation - Hide unnecessary details.
2. Inheritance - Reuse common behavior or Components
3. Polymorphism -Different classes respond to the same method differently.
4. Abstraction - Hiding the complex implementation details and showing only the essential features of the object.
5. 