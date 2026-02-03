"""
course.py
Model for an academic course. The `Course` class stores identifying
information (id, name, instructor, schedule, capacity) and the list of
currently enrolled students. It provides small helper methods used by
the application code to check capacity and manage enrollments.
"""


class Course:
    # OOP - Encapsulation:
    # Course keeps its attributes private to the class and exposes accessor
    # methods (get_course_id, get_course_name, get_instructor, get_schedule,
    # get_max_students) and mutators (add_student, remove_student) to manage state.
    # OOP - Abstraction:
    # Methods like `is_full` provide a simple interface hiding the internal
    # representation of enrolled students.
    def __init__(self, course_id, course_name, instructor, schedule, max_students):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.schedule = schedule
        self.max_students = max_students
        self.enrolled_students = []

    def get_course_id(self):
        return self.course_id

    def get_course_name(self):
        return self.course_name

    def get_instructor(self):
        return self.instructor

    def get_schedule(self):
        return self.schedule

    def get_max_students(self):
        return self.max_students

    def get_enrolled_students(self):
        return self.enrolled_students

    def is_full(self):
        return len(self.enrolled_students) >= self.max_students

    def add_student(self, student):
        self.enrolled_students.append(student)

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)