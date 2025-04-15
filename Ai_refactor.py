def display_menu():
    """Display the main menu options."""
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")


def add_task(task_list):
    """Add tasks to the task list until the user types 'done'."""
    print("Press enter to save each task. Type 'done' when finished.")
    while True:
        new_task = input("Task: ").strip()
        if new_task.lower() == "done":
            break
        task_list.append(new_task)


def delete_task(task_list):
    """Delete tasks from the task list based on user input."""
    if not task_list:
        print("Task List is empty.")
        return

    print("Current Tasks:")
    for task in task_list:
        print(f"- {task}")

    while True:
        to_delete = input("Enter task to delete (or type 'done' to finish): ").strip()
        if to_delete.lower() == 'done':
            break
        if to_delete in task_list:
            task_list.remove(to_delete)
            print(f"Deleted: {to_delete}")
        else:
            print("Task not found: check spelling.")


def view_tasks(task_list):
    """Display the current list of tasks."""
    if not task_list:
        print("Task List is empty.")
    else:
        print("Current Tasks:")
        for task in task_list:
            print(f"- {task}")


def to_do_application():
    """Main function to run the to-do list CLI application."""
    task_list = []
    print("Welcome to the To-Do List Application!")

    while True:
        try:
            display_menu()
            menu_option = int(input("Select an option (1-4): "))

            if menu_option == 1:
                add_task(task_list)
            elif menu_option == 2:
                delete_task(task_list)
            elif menu_option == 3:
                view_tasks(task_list)
            elif menu_option == 4:
                print("Exiting...")
                break
            else:
                print("Invalid option, please choose 1-4.")

        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    to_do_application()