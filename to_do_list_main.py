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
    Normalised task priority to lowercase.

    Returns:
    dict: The name of the task and priority as entered by the user.
    """
    task_to_add = {}
    while True:
        task_name = input("Enter name of task: ").strip()
        task_priority = input("Enter task priority, low, medium, high or critical: ").strip().lower()
        if task_name and task_priority == "low":
            task_to_add = {"Name": task_name, "Priority": task_priority}
            return task_to_add
        else: 
            print("Task name cannot be empty, please enter a valid task")
    


def remove_from_list(tasks_list):
    """
    Prompts the user for the task they would like to remove from the list of tasks.

    Args:
        list_of_tasks (list): A list of task names.

    Returns:
        None: The function modifies the list in place.
    """
    new_task_list = []
    task_to_remove = input("Please enter the name of the task you would like to remove: ").strip()
    found = False
    # Iterate through each element in the list
    # 
    for task in tasks_list:
        if task["Name"] != task_to_remove:
            new_task_list.append(task)
        else: 
            print(f"Removed {task_to_remove} - Priority {task["Priority"]} from the list")
            found = True
    if not found:
        print(f"Unable to find {task_to_remove} in the list")
    tasks_list.clear()
    tasks_list.extend(new_task_list)
            

def view_tasks(tasks_list):
    """
    Displays the tasks in the provided list line by line.

    If the list is empty, it informs the user the to-do list is empty.

    Args:
        list_of_tasks (list): A list of task names

    Returns:
        None
    """

    if tasks_list:
        for task in tasks_list:
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