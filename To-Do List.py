def todoList():
    tasks = []
    
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            task = input("Enter the task to add:")
            tasks.append(task)
            print("Task added.")
        elif choice == "2":
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")
        elif choice == "3":
            if tasks:
                print("Your Tasks:")
                for t in tasks:
                    print("-", t)
            else:
                print("No tasks in the list.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

todoList()