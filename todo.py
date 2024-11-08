tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def list_tasks():
    for idx, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx + 1}. {task['task']} - {status}")

def mark_task_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

while True:
    print("1. Add Task  2. List Tasks  3. Complete Task  4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task description: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        task_num = int(input("Enter task number to mark complete: ")) - 1
        mark_task_complete(task_num)
    elif choice == "4":
        break
