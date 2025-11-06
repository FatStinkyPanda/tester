"""
Task Manager Module
Handles task operations and coordinates between validator and storage
"""

from validator import TaskValidator
from storage import TaskStorage

class TaskManager:
    def __init__(self):
        self.validator = TaskValidator()
        self.storage = TaskStorage()
        self.tasks = self.storage.load_tasks()

    def add_task(self, title, description, priority):
        """Add a new task with validation"""
        validation_result = self.validator.validate_task(title, description, priority)

        if not validation_result['valid']:
            return f"Validation failed: {validation_result['errors']}"

        task_id = self._generate_id()
        task = {
            'id': task_id,
            'title': title,
            'description': description,
            'priority': priority.lower(),
            'completed': False
        }

        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        return f"Task '{title}' added successfully with ID {task_id}"

    def get_all_tasks(self):
        """Retrieve all tasks"""
        return self.tasks

    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.storage.save_tasks(self.tasks)
                return f"Task {task_id} marked as complete"
        return f"Task {task_id} not found"

    def delete_task(self, task_id):
        """Delete a task by ID"""
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task['id'] != task_id]

        if len(self.tasks) < initial_length:
            self.storage.save_tasks(self.tasks)
            return f"Task {task_id} deleted"
        return f"Task {task_id} not found"

    def _generate_id(self):
        """Generate a unique task ID"""
        if not self.tasks:
            return 1
        return max(task['id'] for task in self.tasks) + 1
