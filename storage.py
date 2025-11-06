"""
Storage Module
Handles reading and writing tasks to persistent storage
"""

import json
import os

class TaskStorage:
    def __init__(self, filename='tasks.json'):
        self.filename = filename

    def load_tasks(self):
        """Load tasks from JSON file"""
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: Could not parse {self.filename}, starting fresh")
            return []
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return []

    def save_tasks(self, tasks):
        """Save tasks to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(tasks, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False

    def clear_all_tasks(self):
        """Clear all tasks (for testing purposes)"""
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return True
