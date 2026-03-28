def save_task(tasks):
    with open("todos.txt", "w") as f:
        for task in tasks:
            f.write(f"{task['name']},{task['status']}\n")

def load_tasks():
    tasks=[]
    try:
        with open("todos.txt", "r") as f:
            for line in f:
                name, status = line.strip().split(",")
                tasks.append({"name": name, "status": status})
    except FileNotFoundError:
        pass
    return tasks

def add_task(tasks):
    name = input("Enter task name: ")
    tasks.append({"name": name, "status": "pending"})
    save_task(tasks)
    print("Task added.")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} - {task['status']}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    num = int(input("Mark which task as done?"))
    tasks[num-1]["status"] = "completed"
    save_task(tasks)

def delete_task(tasks):
    view_tasks(tasks)
    num = int(input("Delete which task?"))
    del tasks[num-1]
    save_task(tasks)

tasks=load_tasks()
while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        mark_task_completed(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        break