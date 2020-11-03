#
# Python: 3.9.0
#
# Author: Maria Hou
#
# Purpose:  This program creates a parent class and then two children
#           classes which inherit the attributes of the parent class
#           with the addition of some unique classes.



class Person:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def welcome_func(self):
        print("Welcome to Central High School {} {}.\n".format(self.fname, self.lname))

p1 = Person("Louisa", "Tennas", "ltennas@chs.com")
p1.welcome_func()


class Student(Person):
    def __init__(self, fname, lname, email, grade, studentID, GPA):
        #allows us to get all the attributes of the parent class
        super().__init__(fname, lname, email)
        self.grade = grade
        self.studentID = studentID
        self.GPA = GPA

    def student_stats(self):
        print("{0} {1} is a {2} who has a {3} GPA and a student ID of {4}.\
        \nThey can be reached at {5}.\n".format(self.fname, self.lname,\
                self.grade, self.GPA, self.studentID, self.email))

p2 = Student("Mike", "Olsen", "molsen@chs.com", "sophomore", 1234, 3.9)
p2.student_stats()


        
class Teacher(Person):
    def __init__(self, fname, lname, email, subject, teacherID):
        # allows us to get all the attributes of the parent class
        super().__init__(fname, lname, email)
        self.subject = subject
        self.teacherID = teacherID

    def teacher_stats(self):
        print("{} {} is a {} teacher who has a teacher ID of {}.\
        \nThey can be reached at {}.\n".format(self.fname, self.lname, self.subject, self.teacherID, self.email))

p3 = Teacher("Tom", "Laner", "tlaner@chs.com", "history", 1000)
p3.teacher_stats()
