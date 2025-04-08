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
    
    def __gt__(self, other):
        if(self.m1 > other.m1 and self.m2 > other.m2):
            print('A winds')
        elif((self.m1 > other.m1 and self.m2 < other.m2 )or (self.m1 < other.m1 and self.m2 > other.m2 )):
            print('Draw')
        else:
            print('B wins')
    
    # comparing students with '>'
    # if both the marks of student A > studetn B,  -> A wins
    # else B. wins
    # if one mark is greater and ohter is smalller then Draws

    
s1=Student(66, 69)
s2=Student(60, 65)

s3=s1+s2
s4=s1-s2
print(s3.m1, s3.m2)
print(s4.m1, s4.m2)

# same thing can be done with *,/,>=, <=

# notice we had also changed the retudrn type of '>' symbol, now its not returning bool
# but printing thing sonly

s1 > s2


# ----------------------------------------------------------------------------------------------------
# changing the behaviour of print(class Object)
# generally print('className) gives type of the vraible

intVar=9
print(intVar)          # Prints the value
print(intVar.__str__())


# Note : can't use __str__() with class while using print()
class x:
    pass
print(x)               # Prints the type(for a class, since its has not been given space in memory)

x1=x()
print(x1.__str__())
print(x1)              # Prints the type with Address(for an object)

# Note : whenever u call 'print(IntVar)' it will call 'print(IntVar.__str__())' to get the value/address/type
# .__str__() function is automatically called on using any variable

# Thus the __str__() behaves differently while using print() with a variable
# if you want to print the value of an object of class, just change/Override this variable

print('---------Changing the Behaviour of object at print() -------------------------')

class y:
    def __init__(self, mag):
        self.val=mag

    def __str__(self):
        return str(self.val)           # if we don't return str val, it can't be printed

y1=y(87)
print(y1) 

# can easily print a integer returned value, easily
class temp:
    def fn(self):
        return 8
    
temp1=temp()
print(temp1.fn())
