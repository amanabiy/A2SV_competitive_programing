from collections import defaultdict 
class Student:
    def __init__(self, age, studId, grade):
        """inistantiate class"""
        self.__age = self.set_age(age)
        self.STUDENT_ID = self.set_STUDENT_ID(studId)
        self.grade = self.set_grade(grade)


    def set_age(self, age):
        if age > 17 and age < 35:
            self.__age = age

    def get_age(self):
        return self.__age

    def set_STUDENT_ID(self, studId):
        self.STUDENT_ID = studId

    def get_STUDENT_ID(self):
        return self.STUDENT_ID
    
    def set_grade(self, grade):
        self.grade = grade
        print(self.grade.values())
        return self.grade
    
    def get_grade(self):
        return self.grade

    def compare(self, stud, subject):
        return True if self.get_grade()[subject] > stud.get_grade()[subject] else False
    
    def average(self):
        print(self.get_grade())
        return sum(self.get_grade().values()) / len(self.get_grade())

    def __gt__(self, stud):
        average1 = self.average()
        average2 = stud.average()
        return True if average1 > average2 else False

    def __lt__(self, stud):
        average1 = self.average()
        average2 = stud.average()
        return True if average1 < average2 else False

    def grade_report(self):
        print("student ID:", self.get_STUDENT_ID)
        print("student age:", self.get_age)
        for key, subject in self.get_grade:
            print(key, subject)

    def __str__(self):
        return "to be implemented"



grade = defaultdict(int)
grade2 = defaultdict(int)
grade.update({
    "english": 80,
    "math": 100,
    "programming": 90
})
grade2.update({
    "english": 90,
    "math": 70,
    "programming": 60
})

student1 = Student(20,2398,grade)
student2 = Student(25,765,grade2)
student2.set_age
print(student2.grade)
print(student2)
print(student1 > student2)
print(student1 < student2)