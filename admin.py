from user import User
from course import Course


class Admin(User):
    # OOP - Inheritance:
    # Admin inherits from User so it shares authentication methods and identity.
    # OOP - Abstraction:
    # Admin provides higher-level operations (create_course, delete_course,
    # view_all_courses) that encapsulate the underlying Course operations.
    def __init__(self, username, password, admin_id):
        super().__init__(username, password, admin_id)

    def create_course(self, course_id, course_name, instructor, schedule, max_students):
        return Course(course_id, course_name, instructor, schedule, max_students)

    def delete_course(self, courses, course_id):
        for course in courses:
            if course.get_course_id() == course_id:
                if not course.get_enrolled_students():
                    courses.remove(course)
                    return True
                else:
                    print("Cannot delete course with enrolled students.")
                    return False

        print("Course not found.")
        return False

    def view_all_courses(self, courses):
        if not courses:
            print("No courses available.")
            return

        print("\nAll Available Courses:")
        print("------------------------------------------------------------------")
        print(f"{'Course ID':<15} {'Course Name':<20} {'Instructor':<15} "
              f"{'Schedule':<15} {'Capacity':<10} {'Enrolled':<10}")
        print("------------------------------------------------------------------")

        for course in courses:
            print(f"{course.get_course_id():<15} "
                  f"{course.get_course_name():<20} "
                  f"{course.get_instructor():<15} "
                  f"{course.get_schedule():<15} "
                  f"{course.get_max_students():<10} "
                  f"{len(course.get_enrolled_students()):<10}")

        print("------------------------------------------------------------------")
        print(f"Total courses: {len(courses)}")