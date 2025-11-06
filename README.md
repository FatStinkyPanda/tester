# Task Manager Tester

A simple multi-file task management program designed for testing memory and validation systems.

## Features

- Add, list, complete, and delete tasks
- Edit existing tasks (title, description, priority)
- Search tasks by title or description
- Filter tasks by priority and completion status
- View task statistics and completion rates
- Timestamp tracking (created_at, completed_at)
- Data validation across multiple components
- Persistent storage using JSON
- Clean separation of concerns across multiple files
- Enhanced error handling with try-catch blocks

## Files

- `main.py` - Entry point and user interface
- `task_manager.py` - Core task management logic
- `validator.py` - Input validation
- `storage.py` - Persistent storage handler
- `tasks.json` - Data storage (auto-generated)

## Usage

Run the program:
```
python main.py
```

## Testing Memory & Validation

This program is ideal for testing memory systems because it:
- Maintains state across multiple operations
- Uses validation logic that can be tracked
- Has multiple interconnected files
- Performs various CRUD operations
- Stores persistent data
- Tracks timestamps for all operations

Perfect for validating that memory systems can track:
- Function calls across modules
- Data flow between components
- Validation rules and their application
- State changes over time
- User interaction patterns
