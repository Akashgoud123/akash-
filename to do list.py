tasks = []
def display_tasks():
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def update_task():
    display_tasks()
    task_num = int(input("Enter the task number to update: ")) - 1
    if task_num < len(tasks):
        task = input("Enter the updated task: ")
        tasks[task_num] = task
        print(f"Task '{task}' updated!")
    else:
        print("Invalid task number!")

def delete_task():
    display_tasks()
    task_num = int(input("Enter the task number to delete: ")) - 1
    if task_num < len(tasks):
        del tasks[task_num]
        print("Task deleted!")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
