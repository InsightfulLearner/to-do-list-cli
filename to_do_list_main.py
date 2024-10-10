"""
This is an app which lets you implement and track a to-do list
You can add, remove and view the list
"""

import sys
import time


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


def add_to_list():
    """
    Prompts the user to enter the name of the task they would like to add.
    Any additional whitespace is removed with the .strip()

    Returns:
    str: The name of the task as entered by the user.
    """

    while True:
        task_to_add = input("Enter name of task: ").strip()
        if task_to_add:
            return task_to_add
        else: 
            print("Task name cannot be empty, please enter a valid task")
    


def remove_from_list(list_of_tasks):
    """
    Prompts the user for the task they would like to remove from the list of tasks.

    Args:
        list_of_tasks (list): A list of task names.

    Returns:
        None: The function modifies the list in place.
    """

    task_to_remove = input("Please enter the name of the task you would like to remove: ").strip()
    if task_to_remove in list_of_tasks:
        list_of_tasks.remove(task_to_remove)
        print(f"Task '{task_to_remove}' has been removed")
    else:
        print(f"Task '{task_to_remove}' not found in the list")


def view_tasks(list_of_tasks):
    """
    Displays the tasks in the provided list line by line.

    If the list is empty, it informs the user the to-do list is empty.

    Args:
        list_of_tasks (list): A list of task names

    Returns:
        None
    """

    if list_of_tasks:
        for task in list_of_tasks:
            print(task)
    else:
        print("The to-do list is empty")


def handle_user_selection(user_selection, list):
            # Handles the relevant action based on the users selection
        match user_selection:
            case 1:
                task_to_add = add_to_list()
                list.append(task_to_add)            
            case 2:
                remove_from_list(list)
            case 3:
                view_tasks(list)
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