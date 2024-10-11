"""
This is an app which lets you implement and track a to-do list
You can add, remove and view the list
"""

import sys
import time
import json
import os 

try:
    with open('tasks.json', 'r') as file:
        tasks_data = json.load(file)
        # Ensure it's a list
        if not isinstance(tasks_data, list):
            print("Loaded data is not a list. Initializing an empty task list.")
            tasks_data = []
except FileNotFoundError:
    print("The file does not exist")
    tasks_data = []
except json.JSONDecodeError:
    print("Error decoding JSON")
    tasks_data = []


def store_task_in_file(tasks_data):
    with open("tasks.json", "w") as file:
        json.dump(tasks_data, file, indent = 4)


def show_menu():
    """
    Displays a menu to the user for task management.
    
    Prompts the user to select an option (1-4). If the input is not an integar
    or is out of range, the user will be prompted again.

    Returns:
    int: The user's selection (1 to 4)
    """

    while True:

        try:
            user_input = int(input( "Press 1 to add a task\n"
                                    "Press 2 to remove a task \n"
                                    "Press 3 to view all tasks \n"
                                    "Press 4 to exit \n"))
        except ValueError:
            print("Did not enter an integer")
            continue

        if user_input < 1 or user_input > 4:
            print("Invalid selection")
        else:
            break

    return user_input


def add_to_list() -> None:
    """
    Prompts the user to enter the name of the task they would like to add.
    Any additional whitespace is removed with the .strip()
    Normalised task priority to lowercase.

    Returns:
        None
    """

    while True:
        
        task_name = input("Enter name of task: ").strip()

        if task_name == "":
            print("No task name entered")
            continue

        task_priority = input("Enter task priority: Low, Medium, "
                              "High or Critical: ").strip().lower()
        
        if task_priority not in {"low", "medium", "high", "critical"}:
            print("Invalid priority entered")
            continue

        task_priority_capitalized = task_priority.capitalize()
        file_to_store = {"Name": task_name, "Priority":task_priority_capitalized}
        tasks_data.append(file_to_store)
        store_task_in_file(tasks_data)
        break

    
def remove_from_list():
    """
    Prompts the user for the task they would like to remove from the list of tasks.

    Args:
        list_of_tasks (list): A list of task names.

    Returns:
        None: The function modifies the list in place.
    """
    global tasks_data
    task_to_remove = input("Please enter the name of the task you would like to remove: ").strip()
    new_task_list = [task for task in tasks_data if task["Name"] != task_to_remove]

    if len (new_task_list) < len(tasks_data):
        print(f"Removed {task_to_remove} from task list")
        tasks_data = new_task_list
        store_task_in_file(tasks_data)
    else:
        print(f"Unable to find {task_to_remove} in the list")
    
            
def view_tasks():
    """
    Displays the tasks in the provided list line by line.

    If the list is empty, it informs the user the to-do list is empty.

    Args:
        list_of_tasks (list): A list of task names

    Returns:
        None
    """
    for task in tasks_data:
        print(f"Task name: {task['Name']} - Priority: {task['Priority']}")


def handle_user_selection(user_selection, task_list):
        # Handles the relevant action based on the users selection
        match user_selection:
            case 1:
                add_to_list()           
            case 2:
                remove_from_list()
            case 3:
                view_tasks()
                time.sleep(3)
            case 4:
                sys.exit()


def main():
    list_of_tasks = [] # create empty list to be used

    # Loops the menu until the user enters the input to exit (4)
    while True:

        print("To-do list")
        user_input = show_menu() # Shows menu to user, returns their choice as int
        handle_user_selection(user_input, list_of_tasks)


if __name__ == "__main__":
    main()