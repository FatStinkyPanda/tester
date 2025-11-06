"""
Validator Module
Validates task data before processing
"""

class TaskValidator:
    VALID_PRIORITIES = ['low', 'medium', 'high']

    def validate_task(self, title, description, priority):
        """Validate task data"""
        errors = []

        # Validate title
        if not title or len(title.strip()) == 0:
            errors.append("Title cannot be empty")
        elif len(title) > 100:
            errors.append("Title cannot exceed 100 characters")

        # Validate description
        if not description or len(description.strip()) == 0:
            errors.append("Description cannot be empty")
        elif len(description) > 500:
            errors.append("Description cannot exceed 500 characters")

        # Validate priority
        if not priority or priority.lower() not in self.VALID_PRIORITIES:
            errors.append(f"Priority must be one of: {', '.join(self.VALID_PRIORITIES)}")

        return {
            'valid': len(errors) == 0,
            'errors': errors
        }

    def validate_id(self, task_id):
        """Validate task ID"""
        if not isinstance(task_id, int) or task_id < 1:
            return {
                'valid': False,
                'errors': ["Task ID must be a positive integer"]
            }
        return {'valid': True, 'errors': []}
