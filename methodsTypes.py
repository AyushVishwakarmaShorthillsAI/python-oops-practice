# 3 types of methods 
# 1) Instance methods
# 2) Class methods
# 3) Static methods(note: static != class like in variables types)

class student:
    school='SAPS'

    def __init__(self):
        self.name="Ayush"
        self.age=18
        self.marks_Physics=95
        self.marks_Math=95
        self.marks_Chem=95
        self.marks_Comp=91

    # for making a class method, need 'cls' parameter
    # for instance method -> 'self' pararmeter

    # for class methods, we also need to specify it using Decorators

    @classmethod
    def getSchool(cls):
        print(cls.school)
    
    @staticmethod
    def info():
        print('This is the info regaring class _Student_, made on April 7, 2025 at around 12:55 PM')

s1=student()
s2=student()

student.getSchool()