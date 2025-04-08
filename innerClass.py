# class inside a class

class student:
    def __init__(self):
        self.rollNo=1
        self.name='AYush'
        self.lap=student.Laptop()

    
    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.model='Victus'
            self.proceesor='Ryzen 5600 H'
            self.ram='8 GB'
        

    def lapInfo(self):
        print(f"Laptop name : {self.lap.brand}", end=" ");
        print(self.lap.model)
        print(f"Laptop processor: {self.lap.proceesor}")
        print(f"Laptop ram size : {self.lap.ram}")


# Q) Why we are able to use Laptop() and make an obejct before defining the Laptop class itself ? Also, the flow here in python is from Top to Down
# A) bcoz, the lines of codes inside __init__ are called at the time of its object creation only i.e at s1=student()

s1=student()
print(f'Info of laptop for student : {s1.name}, roll no. is {s1.rollNo}')
s1.lapInfo()

# ----------------------------------------------------------------------------------------------------
# can also change the info of laptoop below 
s1.lap.proceesor='Zyzen 5 5800 H'
s1.lapInfo()

# the format to access class within a class is : 
# (object/class).innerClass.(member/funciton)

# -----------------------------------------------------------------------------------------------------------
# Why don't create a outer class and use it in the upper class 
# When the inner class is not to be used anywhere else than in only one class 

# -----------------------------------------------------------------------------------------------------------------------
# Creating the inner class outside
print('making inner class object outside the parent class')
lap4=student.Laptop()
# lap4.lapInfo()      # can't use it since the funciton is for the student class
print(lap4.brand)
print(lap4.model)