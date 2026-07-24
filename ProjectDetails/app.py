import sqlite3
import questionary
from add_task import add_task
from view_task import view_task
from update_task import update_task
from delete_task import delete_task

def task():
    prompt= questionary.select(
        "What would you like to do?",
        choices=[
            "Add Task",
            "View Tasks",
            "Update Task",
            "Delete Task",
            "Exit"
        ]
    ).ask()
    if prompt == "Add Task":
        add_task()
        task()
    elif prompt == "View Tasks":
        view_task()
        task()
    elif prompt == "Update Task":
        update_task()
        task()
    elif prompt == "Delete Task":
        delete_task()
    elif prompt == "Exit":
        exit

task()