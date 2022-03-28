class DataSheet():
    def __init__(self, courses =[]):
        self.courses = []
        for course in courses:
            self.courses.append(course)

    def add_course(self, course):
        self.courses.append(course)

    def get_grades_as_list(self):
        grade_list = []
        for course in self.courses:
            grade_list.append(int(course.grade))
        return grade_list