class ToDoListManager:
    def __init__(self):
        self.to_do_list = []

    def add_task(self, task):
        self.to_do_list.append({"task": task, "status": "Pending"})

    def list_tasks(self):
        return self.to_do_list

    def mark_task_completed(self, task):
        for t in self.to_do_list:
            if t["task"] == task:
                t["status"] = "Completed"
                break

    def clear_list(self):
        self.to_do_list = []

if __name__ == "__main__":
    manager = ToDoListManager()
    while True:
        command = input("Enter command (add/list/mark/clear/exit): ").strip().lower()
        if command == "add":
            task = input("Enter task: ")
            manager.add_task(task)
        elif command == "list":
            tasks = manager.list_tasks()
            for task in tasks:
                print(f"{task['task']} - {task['status']}")
        elif command == "mark":
            task = input("Enter task to mark as completed: ")
            manager.mark_task_completed(task)
        elif command == "clear":
            manager.clear_list()
        elif command == "exit":
            break
        else:
            print("Unknown command.")
