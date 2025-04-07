# your parent's things are your things

# How to inherit ?
# Just give the name of class to act as parent in the parenthesis while writing the class definition

class A:
    def f1(self):
        print('this is feature 1')

    def f2(self):
        print('this is feature 2')

class B(A):
    def f3(self):
        print('this is feature 3')

    def f4(self):
        print('this is feature 4')
    

# Syntax : class B(A)
# Here, B is child class and A is parent class

b1=B()
b1.f1()
b1.f2()
b1.f3()
b1.f4()

# The above inheritance is k/a single inheritence

# --------------------------------------------------------------------------------------
# Below is Multilevel inheritance:

class C(B):
    def f5(self):
        print('this function is for class C to denote multilevel inheritance')   


print('Multilevel inheritance as class C inherits all from B and A : ')
c1=C()
c1.f1()
c1.f4()
c1.f5()