"""
Simple Task Manager - Main Entry Point
A multi-file program for testing memory and validation systems
"""

from task_manager import TaskManager

def display_menu():
    print("\n=== Task Manager ===")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 20)

def main():
    manager = TaskManager()

    print("Welcome to the Task Manager!")
    print(f"Currently tracking {len(manager.get_all_tasks())} tasks")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            description = input("Task description: ").strip()
            priority = input("Priority (low/medium/high): ").strip()

            result = manager.add_task(title, description, priority)
            print(f"\n{result}")

        elif choice == "2":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("\nNo tasks found!")
            else:
                print(f"\n{len(tasks)} task(s):")
                for task in tasks:
                    status = "✓" if task['completed'] else " "
                    print(f"  [{status}] {task['id']}: {task['title']} ({task['priority']})")
                    print(f"      {task['description']}")

        elif choice == "3":
            task_id = input("Enter task ID to complete: ").strip()
            result = manager.complete_task(int(task_id))
            print(f"\n{result}")

        elif choice == "4":
            task_id = input("Enter task ID to delete: ").strip()
            result = manager.delete_task(int(task_id))
            print(f"\n{result}")

        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
