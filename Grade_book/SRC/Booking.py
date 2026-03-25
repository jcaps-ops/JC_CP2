class Book:
    def __init__(self,name):
        self.name = name
        self.students = []

    def add_student(self,st):
        self.students.append(st)
    def display_students(self):
        for x in self.students:
            print(f"student number:{x[1]}")

class student:
    def __init__(self,name,id,grades):
        self.name = name
        self.id = id
        self.grades = grades