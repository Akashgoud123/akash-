# todo.py

tasks = []  # List to store tasks

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks yet!")

def main():
    while True:
        print("\nTo-Do List:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


'''
output:
PS D:\akash internship> & C:/Users/akash/AppData/Local/Microsoft/WindowsApps/python3.12.exe "d:/akash internship/to do list.py"

To-Do List:
1. Add Task
2. View Tasks
3. Exit
Enter your choice: 1
Enter the task: drink milk everyday
Task 'drink milk everyday' added successfully!

To-Do List:
1. Add Task
2. View Tasks
3. Exit
Enter your choice: 2
Your tasks:
1. drink milk everyday

To-Do List:
1. Add Task
2. View Tasks
3. Exit
Enter your choice: 3
Goodbye!
PS D:\akash internship>
'''