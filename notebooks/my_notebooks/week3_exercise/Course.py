class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade;

    def __repr__(self):
        return '{%r, %r, %r, %r, %r}' % (self.name, self.teacher, self.classroom, self.ETCS, self.grade)