

from course import Course

class Student:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.enrolled_courses = []
        self.completed_courses= []

    def enroll(self,course):
        if course in self.enrolled_courses:
            return False
        if course.add_student(self):
            self.enrolled_courses.append(course)
            return True
    def unenroll(self,course):
        if course not in self.enrolled_courses:
            return False
        if  course.remove_student(self):
            self.enrolled_courses.remove(course)
            return True
        else:
            return False
    def complete_course(self,course):
        if course not in self.enrolled_courses:
            return False
        if course.mark_completed(self):
            self.enrolled_courses.remove(course)
            self.completed_courses.append(course)
            return True 
        else:
            return False
