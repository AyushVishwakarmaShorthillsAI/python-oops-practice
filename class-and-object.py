# class keyword is used to define a class
# any variable is an object of some class

class computer:
    def config(self):
        print('i5, 16gB, 1 TB')


# self keyword is suggesting that the function will take an object of class 'name' for its working
# 2 ways of calling a function of a class

# Syntax : " computer.config('object_name')  "

# How to make an object of a class, since python is a dynamically typed language, how to create 
# an object without defining its class datatype 
# ans -> Use CONSTRUCTOR

# Syntax to make an object: " varName = className() "
# the className() is a "Constructor"


comp1 = computer()


#calling a function for this comp1 object
computer.config(comp1)
# see here the 'comp1' is being send to the 'self' as an argument

# another way to call a method of class is directly using an object of the class
# for eg :
print('Other way to call a method of class: ')
comp1.config()
# It works in a similar way to the above style, just the object before '.' is passed to the self as its internal working


# -------------------------------------------------------------------------------------------------------------------------------------------------

# How all varaibles are objects of some class
x=8
str1='ayush'

print(type(x))
print(type(str1))
# see how above types are similar as of type of object of class 'computer'
print(type(comp1))