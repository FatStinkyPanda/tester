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
    print("5. Edit Task")
    print("6. Search Tasks")
    print("7. Filter Tasks")
    print("8. View Statistics")
    print("9. Exit")
    print("=" * 20)

def main():
    manager = TaskManager()

    print("Welcome to the Task Manager!")
    print(f"Currently tracking {len(manager.get_all_tasks())} tasks")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-9): ").strip()

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
            try:
                task_id = int(input("Enter task ID to complete: ").strip())
                result = manager.complete_task(task_id)
                print(f"\n{result}")
            except ValueError:
                print("\nInvalid ID. Please enter a number.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                result = manager.delete_task(task_id)
                print(f"\n{result}")
            except ValueError:
                print("\nInvalid ID. Please enter a number.")

        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to edit: ").strip())
                print("Leave blank to keep current value")
                title = input("New title: ").strip()
                description = input("New description: ").strip()
                priority = input("New priority (low/medium/high): ").strip()

                result = manager.edit_task(
                    task_id,
                    title if title else None,
                    description if description else None,
                    priority if priority else None
                )
                print(f"\n{result}")
            except ValueError:
                print("\nInvalid ID. Please enter a number.")

        elif choice == "6":
            query = input("Enter search query: ").strip()
            tasks = manager.search_tasks(query)
            if not tasks:
                print("\nNo matching tasks found!")
            else:
                print(f"\nFound {len(tasks)} matching task(s):")
                for task in tasks:
                    status = "✓" if task['completed'] else " "
                    print(f"  [{status}] {task['id']}: {task['title']} ({task['priority']})")
                    print(f"      {task['description']}")

        elif choice == "7":
            print("\nFilter by:")
            print("1. Priority")
            print("2. Completion status")
            print("3. Both")
            filter_choice = input("Choose filter type: ").strip()

            filter_params = {}
            if filter_choice in ["1", "3"]:
                priority = input("Priority (low/medium/high): ").strip().lower()
                if priority in ['low', 'medium', 'high']:
                    filter_params['priority'] = priority

            if filter_choice in ["2", "3"]:
                status = input("Status (completed/pending): ").strip().lower()
                if status == "completed":
                    filter_params['completed'] = True
                elif status == "pending":
                    filter_params['completed'] = False

            tasks = manager.get_all_tasks(filter_by=filter_params)
            if not tasks:
                print("\nNo tasks match the filter!")
            else:
                print(f"\n{len(tasks)} filtered task(s):")
                for task in tasks:
                    status = "✓" if task['completed'] else " "
                    print(f"  [{status}] {task['id']}: {task['title']} ({task['priority']})")
                    print(f"      {task['description']}")

        elif choice == "8":
            stats = manager.get_statistics()
            print("\n=== Task Statistics ===")
            print(f"Total tasks: {stats['total']}")
            print(f"Completed: {stats['completed']}")
            print(f"Pending: {stats['pending']}")
            print(f"Completion rate: {stats['completion_rate']:.1f}%")
            print(f"\nBy Priority:")
            print(f"  Low: {stats['by_priority']['low']}")
            print(f"  Medium: {stats['by_priority']['medium']}")
            print(f"  High: {stats['by_priority']['high']}")

        elif choice == "9":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
