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

# how to call the static methods, using 'class' or 'object' name ?
student.info()
s1.info()
print('both className or ObjectName can be used to call the static methods as they are not properties of class or objectsd')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------PASSING VALUES TO INIT(CONSTRUCTOR) WHILE CREATING AN OBJECT----------------------------------------

class pen:

    @classmethod
    def info(cls):
        return " THis is info about the class pen, made at 3:35 on APril 7th 2025"

    def __init__(self, brand, color, price):
        self.brand=brand
        self.color=color
        self.price=price
    
    def getInfo(self):
        print('brand is :', self.brand)
        print('color is :', self.color)
        print('price is :', self.price)

    @staticmethod
    def temp():
        return "this is temp static method, can be envoked by any className or methodName"
    

p1=pen('Luxur', 'blue', '65 Rs')
p2=pen('Linc', 'black', '15 Rs')

p1.getInfo()
p2.getInfo()

print(pen.info())

print(pen.temp())
print(p2.temp())

    

