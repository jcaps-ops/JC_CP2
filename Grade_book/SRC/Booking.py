import random
class Book:
    def __init__(self,name):
        self.name = name
        self.students = []

    def add_student(self,StName,StId,StGrades,StAva,StLET):
        temp_student = [StName,StId,StGrades,StAva,StLET]
        self.students.append(temp_student)
    def display_students(self):
        print(f"------------------------------\n| ID | Name | Avarge | GRADE |\n------------------------------")
        for x in self.students:
            print(f"| {x[1]} | {x[0]} | {x[3]} | {x[4]} |")
    def update(self):
         temp_list = []
         duoble = ["Empty"]
         for x in self.students:
            if x[0] not in temp_list:
                temp_list.append(x[0])
            else:
                duoble = x  
         for z in [temp_list]:
              if z[0] == duoble[0]:
                for x in self.students:
                     if x[0] == z[0]:
                        tempIndex_org = self.students.index(x)
                tempIndex_new = self.students.index(duoble)
                self.students.insert(tempIndex_org,duoble)
                self.students.pop(tempIndex_org-1)
                self.students.pop(tempIndex_new)
                """
                    self.students.pop(tempIndex_org+1)
                    self.students.pop(tempIndex_new)
                """
                

         

class student:
    def __init__(self,name,id,grades):
        self.name = name
        self.id = id
        self.grades = grades
        tempValue = 0
        for y in self.grades:
                tempValue += y
        self.avargeGrade = y/len(grades)
        if self.avargeGrade > 90:
             self.letter = "A"
        elif self.avargeGrade > 80:
             self.letter = "B"
        elif self.avargeGrade > 70:
             self.letter = "C"
        elif self.avargeGrade > 60:
             self.letter = "D"
        else:
             self.letter = "F"
    def New_Grade(self,NewGrade):
        self.grades.append(NewGrade)
        tempValue = 0
        for y in self.grades:
                tempValue += y
        self.avargeGrade = y/len(self.grades)
        if self.avargeGrade > 90:
             self.letter = "A"
        elif self.avargeGrade > 80:
             self.letter = "B"
        elif self.avargeGrade > 70:
             self.letter = "C"
        elif self.avargeGrade > 60:
             self.letter = "D"
        else:
             self.letter = "F"
        

book1 = Book("Book1")
Currentstudent = student("john",random.randrange(0,2000),[random.randrange(0,100),random.randrange(0,100)])
book1.add_student(Currentstudent.name,Currentstudent.id,Currentstudent.grades,Currentstudent.avargeGrade,Currentstudent.letter)
book1.display_students()
Currentstudent = student("Amy",random.randrange(0,2000),[random.randrange(0,100),random.randrange(0,100)])
book1.add_student(Currentstudent.name,Currentstudent.id,Currentstudent.grades,Currentstudent.avargeGrade,Currentstudent.letter)
book1.update()
book1.display_students()
Currentstudent = student("john",random.randrange(0,2000),[random.randrange(0,100),random.randrange(0,100)])
book1.add_student(Currentstudent.name,Currentstudent.id,Currentstudent.grades,Currentstudent.avargeGrade,Currentstudent.letter)
book1.update()
book1.display_students()
