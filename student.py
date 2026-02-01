from user import User


class Student(User):
    def __init__(self, username, password, student_id):
        super().__init__(username, password, student_id)
        self.registered_courses = []

    def register_course(self, course):
        if course.is_full():
            print("Registration failed: Course is full.")
            return

        if self.has_time_conflict(course):
            print("Registration failed: Time conflict with another course.")
            return

        if course in self.registered_courses:
            print("You are already registered for this course.")
            return

        self.registered_courses.append(course)
        course.add_student(self)
        print(f"Successfully registered for: {course.get_course_name()}")

    def drop_course(self, course):
        if course in self.registered_courses:
            self.registered_courses.remove(course)
            course.remove_student(self)
            print(f"Successfully dropped: {course.get_course_name()}")
        else:
            print("You are not registered for this course.")

    def view_registered_courses(self):
        if not self.registered_courses:
            print("You are not registered for any courses.")
            return

        print("\nYour Registered Courses:")
        print("--------------------------------------------------")
        print(f"{'Course ID':<15} {'Course Name':<20} {'Schedule':<15} {'Instructor':<10}")
        print("--------------------------------------------------")

        for course in self.registered_courses:
            print(f"{course.get_course_id():<15} "
                  f"{course.get_course_name():<20} "
                  f"{course.get_schedule():<15} "
                  f"{course.get_instructor():<10}")

        print("--------------------------------------------------")
        print(f"Total registered: {len(self.registered_courses)} courses")

    def has_time_conflict(self, new_course):
        for course in self.registered_courses:
            if course.get_schedule() == new_course.get_schedule():
                return True
        return False

    def get_registered_courses(self):
        return self.registered_courses