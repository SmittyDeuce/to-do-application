

def to_do_application():
    task_list = []
    
    while True:
        try:
            menu_option = input("\nChoose an option:\n1. Add Task\n2. Delete Task\n3. View Tasks\n4. Exit\n")
            int_menu_option = int(menu_option)
            
            if int_menu_option == 4:
                print("Exiting...")
                break

            elif int_menu_option == 1:
                print("press enter to save each task: 'done' when finished")
                while True:
                    new_task = input("Task: ")
                    if new_task.lower() == "done":
                        break
                    else:
                        task_list.append(new_task)
                        
            elif int_menu_option == 2:
                if len(task_list) == 0:
                    print("Task List is empty")
                    continue
                else:
                    print(task_list)

                    while True:
                        to_delete = input("Enter task to delete: 'done' when finished ").strip()
                        
                        if to_delete.lower() == 'done':
                            break

                        found = False  # Flag to track if a task was deleted

                        for task in task_list:
                            if to_delete == task:
                                task_list.remove(task)
                                found = True
                                break

                        if not found:
                            print("Task not found: check spelling")
                            
            elif menu_option == 3:
                pass
            
            else:
                print("Invalid option, please choose 1-4.")

        except ValueError:
            print("Please enter a valid number!")
        
        finally:
            print("Thank you Goodbye")
            
to_do_application()