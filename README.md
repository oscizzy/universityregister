# University Registration System (Python)

This project is a Python version of a University Registration System 

## Features
- Student and Admin login
- Course registration and dropping
- Course creation and deletion
- Data persistence using JSON
- Command-line menu interface

## File Structure
- `main.py` – Program entry point
- `registration_system.py` – Core system logic
- `user.py` – Base user class
- `student.py` – Student functionality
- `admin.py` – Admin functionality
- `course.py` – Course model
- `data.json` – Persistent data storage

## How to Run
1. Open the project folder in VS Code
2. Open the terminal
3. Run:

```bash
python main.py

# data.json Explanation
- Stores all courses, students, and admins.
- Allows the system to persist data between runs.
- Without this file, all data would reset to default sample data each time the program starts.