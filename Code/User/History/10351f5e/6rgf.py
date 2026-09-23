from types import NoneType


class Course:
    def __init__(self,title,description,max_capacity=30):
        self.title= title
        self.description= description
        self.max_capacity= max_capacity
        self.instructor = None
        self.students = []
        self.completed_students = []

    def add_student(self,student):
        if len(self.students) >= self.max_capacity:
            return False
        if student in self.students:
            return False
        else:
            self.students.append(student)
            return True
    def mark_completed(self,student):
        if student not in self.students:
            return False
        else:
            self.students.remove(student)
            self.completed_students.append(student)
            return True
    def assign_instructor(self,instructor):
        self.instructor = instructor
        return True
