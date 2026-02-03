"""
registration_system.py
Core application module that defines the `RegistrationSystem` class and the
`start_registration_system` helper. Responsibilities include:

- Loading and saving persistent data (courses, students, admins).
- Initializing sample data when no data file exists.
- Providing the interactive CLI flow (login, admin/student menus).

This module contains the main program logic; it should be imported by
`main.py` which only delegates startup to `start_registration_system()`.
"""

import json
from student import Student
from admin import Admin
from course import Course


class RegistrationSystem:
    DATA_FILE = "data.json"

    # The RegistrationSystem class coordinates the application's state and
    # user interaction. It keeps lists of `courses`, `students`, and `admins`
    # in memory, provides persistence via JSON file I/O, and exposes
    # methods that implement the CLI menus and helper operations.

    def __init__(self):
        self.courses = []
        self.students = []
        self.admins = []
        self.load_data()
        self.initialize_sample_data()

    # Load data from JSON
    def load_data(self):
        try:
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)

            # Load courses
            for c in data.get("courses", []):
                course = Course(
                    c["course_id"],
                    c["course_name"],
                    c["instructor"],
                    c["schedule"],
                    c["max_students"]
                )
                self.courses.append(course)

            # Load students
            for s in data.get("students", []):
                student = Student(s["username"], s["password"], s["user_id"])
                self.students.append(student)

            # Load admins
            for a in data.get("admins", []):
                admin = Admin(a["username"], a["password"], a["user_id"])
                self.admins.append(admin)

        except FileNotFoundError:
            print("No existing data found. Starting fresh system.")

    # Save data to JSON
    def save_data(self):
        data = {
            "courses": [
                {
                    "course_id": c.get_course_id(),
                    "course_name": c.get_course_name(),
                    "instructor": c.get_instructor(),
                    "schedule": c.get_schedule(),
                    "max_students": c.get_max_students()
                } for c in self.courses
            ],
            "students": [
                {"username": s.get_username(), "password": s.password, "user_id": s.get_user_id()}
                for s in self.students
            ],
            "admins": [
                {"username": a.get_username(), "password": a.password, "user_id": a.get_user_id()}
                for a in self.admins
            ]
        }
        with open(self.DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    # Add sample data if empty
    def initialize_sample_data(self):
        if not self.admins:
            self.admins.append(Admin("admin", "admin123", "A001"))
        if not self.students:
            self.students.append(Student("john", "password1", "S001"))
            self.students.append(Student("emma", "password2", "S002"))
        if not self.courses:
            self.courses.append(Course("CS101", "Introduction to Programming", "Dr. Smith", "MWF 10-11", 30))
            self.courses.append(Course("MATH201", "Calculus I", "Prof. Johnson", "TTH 1-2:30", 25))
            self.courses.append(Course("ENG101", "English Composition", "Dr. Williams", "MWF 2-3", 20))

    # Program entry point
    def run(self):
        print("==== University Registration System ====")
        # OOP - Abstraction:
        # `run` provides the high-level program flow (startup, login, menus)
        # so callers don't need to manage these details.
        current_user = self.login()
        if current_user is None:
            print("Login failed. Exiting system.")
            return

        if isinstance(current_user, Admin):
            self.admin_menu(current_user)
        elif isinstance(current_user, Student):
            self.student_menu(current_user)

        self.save_data()

    # Login function
    def login(self):
        username = input("\nEnter username: ").strip()
        password = input("Enter password: ").strip()

        # OOP - Polymorphism & Inheritance:
        # We iterate over `admins` and `students` and call `login` on each.
        # `login` is implemented on the base `User` class and used polymorphically
        # by Admin and Student instances. This demonstrates usage of the shared
        # interface defined by the parent class.
        for admin in self.admins:
            if admin.login(username, password):
                print(f"\nWelcome Admin: {admin.get_username()}")
                return admin

        for student in self.students:
            if student.login(username, password):
                print(f"\nWelcome Student: {student.get_username()}")
                return student

        print("Invalid credentials.")
        return None

    # Student menu
    def student_menu(self, student):
        while True:
            print("\nSTUDENT MENU")
            print("1. View Available Courses")
            print("2. Register for Course")
            print("3. Drop Course")
            print("4. View My Courses")
            print("5. Logout")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.view_all_courses()
            elif choice == "2":
                self.register_student_for_course(student)
            elif choice == "3":
                self.drop_student_course(student)
            elif choice == "4":
                student.view_registered_courses()
            elif choice == "5":
                student.logout()
                return
            else:
                print("Invalid choice.")

    # Admin menu
    def admin_menu(self, admin):
        while True:
            print("\nADMIN MENU")
            print("1. View All Courses")
            print("2. Create Course")
            print("3. Delete Course")
            print("4. View All Students")
            print("5. Register New Student")
            print("6. Delete Student")
            print("7. Logout")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                admin.view_all_courses(self.courses)
            elif choice == "2":
                self.create_new_course()
            elif choice == "3":
                self.delete_existing_course(admin)
            elif choice == "4":
                self.view_all_students()
            elif choice == "5":
                self.register_new_student()
            elif choice == "6":
                self.delete_student()
            elif choice == "7":
                admin.logout()
                return
            else:
                print("Invalid choice.")

    # View courses
    def view_all_courses(self):
        if not self.courses:
            print("No courses available.")
            return

        print("\nAVAILABLE COURSES:")
        print("------------------------------------------------------------------")
        print(f"{'ID':<10} {'Name':<20} {'Instructor':<15} {'Schedule':<15} {'Capacity':<10}")
        print("------------------------------------------------------------------")
        for c in self.courses:
            print(f"{c.get_course_id():<10} {c.get_course_name():<20} {c.get_instructor():<15} "
                  f"{c.get_schedule():<15} {c.get_max_students():<10}")

    # Register student for course
    def register_student_for_course(self, student):
        self.view_all_courses()
        course_id = input("\nEnter course ID to register: ").strip()
        course = self.find_course_by_id(course_id)
        if course:
            student.register_course(course)
        else:
            print("Course not found.")

    # Drop student course
    def drop_student_course(self, student):
        student.view_registered_courses()
        if not student.get_registered_courses():
            return
        course_id = input("\nEnter course ID to drop: ").strip()
        course = self.find_course_by_id(course_id)
        if course:
            student.drop_course(course)
        else:
            print("Course not found.")

    # Create a new course
    def create_new_course(self):
        print("\nCREATE NEW COURSE")
        course_id = input("Enter Course ID: ").strip()
        course_name = input("Enter Course Name: ").strip()
        instructor = input("Enter Instructor: ").strip()
        schedule = input("Enter Schedule: ").strip()
        try:
            max_students = int(input("Enter Max Students: ").strip())
        except ValueError:
            print("Invalid number. Defaulting to 30.")
            max_students = 30
        self.courses.append(Course(course_id, course_name, instructor, schedule, max_students))
        print("Course created successfully!")

    # Delete course
    def delete_existing_course(self, admin):
        self.view_all_courses()
        course_id = input("\nEnter course ID to delete: ").strip()
        if admin.delete_course(self.courses, course_id):
            print("Course deleted successfully.")

    # View students
    def view_all_students(self):
        if not self.students:
            print("No students registered.")
            return
        print("\nREGISTERED STUDENTS:")
        print("-----------------------------")
        print(f"{'ID':<10} {'Username':<20}")
        print("-----------------------------")
        for s in self.students:
            print(f"{s.get_user_id():<10} {s.get_username():<20}")
        print("-----------------------------")
        print(f"Total students: {len(self.students)}")

    # Register new student
    def register_new_student(self):
        student_id = f"S{len(self.students)+1:03}"
        print(f"\nGenerated Student ID: {student_id}")

        while True:
            username = input("Enter Username: ").strip()
            if not username:
                print("Username cannot be empty.")
            elif self.is_username_taken(username):
                print("Username already exists.")
            else:
                break

        while True:
            password = input("Enter Password (min 6 chars): ").strip()
            if len(password) >= 6:
                break
            print("Password must be at least 6 characters.")

        self.students.append(Student(username, password, student_id))
        print(f"\nStudent registered successfully! Student ID: {student_id}")

    # Delete student
    def delete_student(self):
        self.view_all_students()
        if not self.students:
            return
        student_id = input("\nEnter Student ID to delete: ").strip()
        for student in self.students:
            if student.get_user_id() == student_id:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

    # Helper: find course by ID
    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.get_course_id().lower() == course_id.lower():
                return course
        return None

    # Helper: check if username exists
    def is_username_taken(self, username):
        for u in self.students + self.admins:
            if u.get_username() == username:
                return True
        return False


def start_registration_system():
    """Create a RegistrationSystem instance and start the program.

    This helper keeps object creation out of `main.py` while preserving
    the original program behavior.
    """
    system = RegistrationSystem()
    system.run()