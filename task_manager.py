"""
Task Manager Module
Handles task operations and coordinates between validator and storage
"""

from validator import TaskValidator
from storage import TaskStorage
from datetime import datetime

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
            'completed': False,
            'created_at': datetime.now().isoformat(),
            'completed_at': None
        }

        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        return f"Task '{title}' added successfully with ID {task_id}"

    def get_all_tasks(self, filter_by=None):
        """Retrieve all tasks with optional filtering"""
        if filter_by is None:
            return self.tasks

        filtered = self.tasks

        # Filter by priority
        if 'priority' in filter_by:
            filtered = [t for t in filtered if t['priority'] == filter_by['priority']]

        # Filter by completion status
        if 'completed' in filter_by:
            filtered = [t for t in filtered if t['completed'] == filter_by['completed']]

        return filtered

    def search_tasks(self, query):
        """Search tasks by title or description"""
        query_lower = query.lower()
        return [t for t in self.tasks
                if query_lower in t['title'].lower()
                or query_lower in t['description'].lower()]

    def edit_task(self, task_id, title=None, description=None, priority=None):
        """Edit an existing task"""
        for task in self.tasks:
            if task['id'] == task_id:
                if title:
                    task['title'] = title
                if description:
                    task['description'] = description
                if priority:
                    if priority.lower() not in self.validator.VALID_PRIORITIES:
                        return f"Invalid priority. Must be one of: {', '.join(self.validator.VALID_PRIORITIES)}"
                    task['priority'] = priority.lower()

                self.storage.save_tasks(self.tasks)
                return f"Task {task_id} updated successfully"
        return f"Task {task_id} not found"

    def get_statistics(self):
        """Get task statistics"""
        total = len(self.tasks)
        if total == 0:
            return {
                'total': 0,
                'completed': 0,
                'pending': 0,
                'completion_rate': 0,
                'by_priority': {'low': 0, 'medium': 0, 'high': 0}
            }

        completed = sum(1 for t in self.tasks if t['completed'])
        by_priority = {
            'low': sum(1 for t in self.tasks if t['priority'] == 'low'),
            'medium': sum(1 for t in self.tasks if t['priority'] == 'medium'),
            'high': sum(1 for t in self.tasks if t['priority'] == 'high')
        }

        return {
            'total': total,
            'completed': completed,
            'pending': total - completed,
            'completion_rate': (completed / total) * 100,
            'by_priority': by_priority
        }

    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_at'] = datetime.now().isoformat()
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
