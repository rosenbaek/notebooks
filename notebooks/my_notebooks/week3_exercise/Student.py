class Student():
    def __init__(self, name, gender, dataSheet, image_url):
        self.name = name
        self.gender = gender
        self.dataSheet = dataSheet
        self.image_url = image_url


    def get_avg_grade(self):
        grade_list = self.dataSheet.get_grades_as_list()
        totalSum = 0
        for grade in grade_list:
            totalSum = totalSum + grade
        print(totalSum)
        return totalSum/len(grade_list)

    def etcsProgress(self):
        totalsum = 0
        for course in self.dataSheet.courses:
            totalsum = totalsum + int(course.ETCS)
        return totalsum / 150 * 100
