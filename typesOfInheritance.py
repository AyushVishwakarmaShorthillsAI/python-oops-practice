# single done
# multilevel done

# Multiple bleow : a class will inherit from both 1st and 2nd 
# your parent's things are your things

# How to inherit ?
# Just give the name of class to act as parent in the parenthesis while writing the class definition

class X:
    def f1(self):
        print('Hey, How are you :)')

    def Wtf(self):
        print('say something good that logical :<|')

class B:
    def f1(self):
        print('this is feature 1')

    def f2(self):
        print('this is feature 2')

# Syntax Multiple : Class C(A, B)

class C(B, X):
    def f5(self):
        print('this function is for class C to denote multilevel inheritance')   


print('Multiple inheritance as class C inherits from B and A : ')
c1=C()
c1.f1()
c1.Wtf()

# NOTE : No Ambiguity in Multiple inheritence if same function name
# Method Resolution order(MRO) is used for this 

# ----------------------------------------------------------------------------------------
# Constructors in Inheritance
# Init inheritance : If there is no init in base class, then only the parent class init is called
# if there is init in base class then iniit of parent is not called Automatically(different than C++ OOPS)
# if you want to also call the init of Parent class -> Use Super() keyword and call the parent init

print('-------------------- constructor calling automatically :---------------------------- ')

class Parent:
    def __init__(self):
        print('Pranet init called')

class Child(Parent): 
    def __init__(self):
        super().__init__()
        print("Child Init")

child1=Child()


# ----------------------------------------------------------------------------------------------------------
# MRO : What if we have multiple inheritance and we are using super to call the parent init
# which init will it call 

print('--------------------------Method Resolution Order(MRO)---------------------- ')

#NOTE : Python follow the "Left to Right Order" of method inheritance in case of ambiguiuty 
# thus the left one is taken, and right one method is rejected if both same

class Mom:
     def __init__(self):
        print('Moms DNA')

class Dad: 
    def __init__(self):
        print("Dads DNA")

class Me(Mom, Dad):
    def __init__(self):
        super().__init__()
        print("inehrited qualities of both Mom and Dad")

Ayush=Me()

# We can call any(not only init) parent method, we can use super