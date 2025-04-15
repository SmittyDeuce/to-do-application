def to_do_application():
    # Initialize an empty list to store tasks
    task_list = []
    
    # Infinite loop to keep the application running until the user chooses to exit
    while True:
        try:
            # Display the menu and prompt the user for input
            menu_option = input("\nChoose an option:\n1. Add Task\n2. Delete Task\n3. View Tasks\n4. Exit\n")
            int_menu_option = int(menu_option)  # Convert input to integer
            
            # If user chooses option 4, exit the program
            if int_menu_option == 4:
                print("Exiting...")
                break

            # Option 1: Add tasks to the list
            elif int_menu_option == 1:
                print("Press enter to save each task: type 'done' when finished.")
                while True:
                    new_task = input("Task: ")
                    if new_task.lower() == "done":
                        break  # Stop adding tasks when 'done' is typed
                    else:
                        task_list.append(new_task)  # Add the new task to the list
                        
            # Option 2: Delete a task from the list
            elif int_menu_option == 2:
                if len(task_list) == 0:
                    print("Task List is empty")  # Warn if list is empty
                    continue
                else:
                    print(task_list)  # Show current tasks

                    while True:
                        to_delete = input("Enter task to delete: 'done' when finished ").strip()
                        
                        if to_delete.lower() == 'done':
                            break  # Stop deleting when 'done' is typed

                        found = False  # Flag to track if the task was found and deleted

                        for task in task_list:
                            if to_delete == task:
                                task_list.remove(task)  # Delete task
                                found = True
                                break

                        if not found:
                            print("Task not found: check spelling")  # Notify if task not found
                            
            # Option 3: View all tasks
            elif int_menu_option == 3:
                if len(task_list) == 0:
                    print("Task List is empty")  # Warn if there are no tasks
                    continue
                
                print("Current Tasks:")
                for task in task_list:
                    print(f"Task: {task}")  # Display each task
            
            # Handle any menu choice outside of 1-4
            else:
                print("Invalid option, please choose 1-4.")

        # Catch non-integer input errors
        except ValueError:
            print("Please enter a valid number!")