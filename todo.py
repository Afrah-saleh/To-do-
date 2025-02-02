import os

# File to store tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file if it exists"""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to the file"""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\n✅ No tasks found! Add a new one.")
    else:
        print("\n📌 Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    """Add a new task"""
    task = input("📝 Enter your new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def remove_task(tasks):
    """Remove a completed task"""
    show_tasks(tasks)
    try:
        task_number = int(input("❌ Enter task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            save_tasks(tasks)
            print(f"✅ Task removed: {removed_task}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")
def main():
    """Main loop for the To-Do List app"""
    tasks = load_tasks()

    while True:
        print("\n🔹 To-Do List Menu 🔹")
        print("1️⃣ View Tasks")
        print("2️⃣ Add Task")
        print("3️⃣ Remove Task")
        print("4️⃣ Exit")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting To-Do List. Have a great day!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()