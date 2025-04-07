# two types of variable inside a class
# 1) Instance variable (inside init)
# 2) Class(static) variable(oustide init)

class Car:
    wheels=4

    def __init__(self):
        self.company="BMW"
        self.milage=8
        self.model="i7"

# here model, milage and company are useful properties of an object car
# but the basic property is 4 wheels common to all

c1=Car()
c2=Car()

c2.model="iX1"

# the class(static) variable can be accessed by both class name or obejct name
print('the no. of wheels in today cars : ', Car.wheels)

print(c1.company, c1.model, c1.wheels)
print(c2.company, c2.model, c2.wheels)

# ------------------------------------------------------------------------------------------
# Namespace -> The place where you create and store an object/variable is called namesapce
# we can classify namespace regarding a class as :
# Class Namespace and Instance Namespace

# if you want to modify 'wheels' you need to use class an namespace
Car.wheels=5
c1.wheels=6
print(Car.wheels)
print(c1.wheels)
print(Car.wheels)
print(c1.wheels)

# see above is the difference