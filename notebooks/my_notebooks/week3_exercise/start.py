import matplotlib as mpl
# reset defaults because we change them further down this notebook
mpl.rcParams.update(mpl.rcParamsDefault)
import matplotlib.pyplot as plt


import names
import numpy as np
import csv
from random import randrange
from operator import itemgetter
import Student
import DataSheet
import Course

def generator(numberOfStudents):
    course1 = Course.Course("python", "DB1", "Thomas", 30, 7)
    course2 = Course.Course("security", "DB2", "Daniel", 15, 10)
    course3 = Course.Course("ooa", "DB3", "Kim", 10, 12)
    courses = [course1,course2,course3]
    with open('output.csv', 'w') as output_file:
        output_writer = csv.writer(output_file)
        for i in range(numberOfStudents):
            dataSheet = DataSheet.DataSheet([courses[randrange(0,3)]])
            gender = "male"
            if i%2:
                gender = "female"
            
            student = Student.Student(names.get_full_name(gender=gender), gender, dataSheet, "url")
            for course in student.dataSheet.courses:
                output_writer.writerow([student.name, course.name, course.teacher, student.gender, course.ETCS, course.classroom, course.grade, student.image_url])


def readStudentsFromCSV():
    with open('output.csv') as data:
        content = data.readlines()
        mainDictionary = {}
        for i in content:
            student = i.split(",")
            studentDictionary = mainDictionary.get(student[0], "null")
            if studentDictionary is "null":
                newCourse = Course.Course(student[1],student[2], student[5],student[4],student[6] )
                newDataSheet = DataSheet.DataSheet([newCourse])
                newStudent = Student.Student(student[0], student[3],newDataSheet,student[7])
                mainDictionary[student[0]] = newStudent
            else:
                newCourse = Course.Course(student[1],student[2], student[5],student[4],student[6] )
                studentDictionary.dataSheet.add_course(newCourse)
     
        studentList = []
        for studentName, studentInfo  in mainDictionary.items():
            tempStudent = {"name": studentName, "url": studentInfo.image_url, "avgGrade":studentInfo.get_avg_grade(), "ectsProgress": studentInfo.etcsProgress()}
            studentList.append(tempStudent)
        return studentList

def createBarChartGrade(data):
    sortedData = sorted(data, key=itemgetter('avgGrade'))
    mpl.use("pdf")
    x_values = []
    y_values = []

    for student in sortedData:
        x_values.append(student['name'])
        y_values.append(student['avgGrade'])        
    plt.bar(x_values, y_values, width=0.5, align="center")    
    plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')
    plt.savefig('barchartGrade.png',bbox_inches='tight')

def createBarChartETCS(data):
    sortedData = sorted(data, key=itemgetter('ectsProgress'))
    mpl.use("pdf")
    x_values = []
    y_values = []

    for student in sortedData:
        x_values.append(student['name'])
        y_values.append(student['ectsProgress'])        
    plt.bar(x_values, y_values, width=0.5, align="center")    
    plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')
    plt.savefig('barchartETCS.png',bbox_inches='tight')

if __name__ == '__main__':
    generator(5)
    data = readStudentsFromCSV()
    createBarChartGrade(data)
    createBarChartETCS(data)
   