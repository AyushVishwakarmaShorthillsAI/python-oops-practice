# operator overloading means changing the behaviour of operators(symbols)

a=5
b=4

# string do not support '-' but support concatenation using '+'
# if we can use '-' for remove a substring from another string, it will be 
# overloading of - operator

# we can do this easily since internally the opeartors are calling a function 
# example : both below are similar
print(a + b)
print(int.__add__(a,b))

x='ayush'
y='Bro'
print(x+y)
print(str.__add__(x,y))

# __add__(x,y)
# __sub__(s,y)
# __mul__(s,y)
# all according to datatypes

# Note : we can simply overiride the add function in a paritcular class
# for eg. __add__(a,b) function to a class to overiride the functioality of the + operator

print('--------Overriding Add function in class to do Operator Overloading-----------')

# an exmaple to override the add operator
class Student:
    def __init__(self, m1, m2):
        self.m1=m1
        self.m2=m2

    # behind the scene the below function is getting converted into :
    # Student.__add__(s1, s2)  where   s1=self and s2=another
    def __add__(self, other):
        x=self.m1+other.m1
        y=self.m2+other.m2

        s3=Student(x,y)
        return s3
    
    def __sub__(self, other):
        x=self.m1-other.m1
        y=self.m2-other.m2

        s3=Student(x,y)
        return s3

    
s1=Student(58, 69)
s2=Student(60, 65)

s3=s1+s2
s4=s1-s2
print(s3.m1, s3.m2)
print(s4.m1, s4.m2)
