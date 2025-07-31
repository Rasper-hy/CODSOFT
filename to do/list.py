# To-Do List Application

TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks to show.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions: [1] Show Tasks  [2] Add Task  [3] Remove Task  [4] Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added.")

        elif choice == "3":
            show_tasks(tasks)
            try:
                task_number = int(input("Enter the number of the task to remove: ")) - 1
                removed_task = tasks.pop(task_number)
                save_tasks(tasks)
                print(f"Removed: {removed_task}")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == "4":
            print("Exiting... Have a productive day!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()