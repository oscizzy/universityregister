class Course:
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