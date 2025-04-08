# (Method Overloading Vs Merhod Overriding )in Polymorphism

# Java, C++ have method overloading there, But not Python have
# --------------Python Don't have Method Overloading-------------------
# Can't create 2 functions of same name in python

# Method Overloading -> the pararmeters of function will  be diffeermt
# Metood Overridinng -> the parameters and name of function will be same

# Q) Why not Method Overloading ?
# A) This is because, we can use specail things of python like *args, **kwargs
# or can set the extra parameters to none

def sum(a=None, b=None, c=None):
    if(a==None and b==None and c==None):
        return 0
    
    print('above ran')
    s=0
    
    if(a):
        s+=a
    if(b):
        s+=b
    if(c):
        s+=c

    return s

print(sum(1,4))

# the above function can work for 2, 3 or 1 arguments, thuse
# we are not required to make different function for the same
# similarly we can use kwargs to bypass overloading

def sum(a=0, b=0, c=0, d=0, e=0):
    return a+b+c+d+e

print(sum(1, 2, 6))


# See the above scenerio, the sum function has not been overloaded, But OVERRIDED
# Same FUNCTION NAME WILL CAUSE METHOD OVERRIDING -> NO OVERLOADING

# DEFINITION A NEW OBJECT WITH SAME NAME, ALWAYS CAUSES METHOD OVERRIDING