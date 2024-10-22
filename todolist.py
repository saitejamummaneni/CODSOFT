import sqlite3

conn = sqlite3.connect('tasks.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, task TEXT)''')

def add_task(task):
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    print(f"Added task: {task}")

def remove_task(task_id):
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    print(f"Removed task with ID: {task_id}")

def view_tasks():
    c.execute("SELECT * FROM tasks")
    for row in c.fetchall():
        print(f"{row[0]}. {row[1]}")

while True:
    command = input("Enter a command (add, remove, view, exit): ").strip().lower()
    
    if command == "add":
        task = input("Enter a task to add: ").strip()
        add_task(task)
    elif command == "remove":
        task_id = int(input("Enter the task ID to remove: ").strip())
        remove_task(task_id)
    elif command == "view":
        view_tasks()
    elif command == "exit":
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid command. Please try again.")
