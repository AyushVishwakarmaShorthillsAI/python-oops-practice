# Python by default don't support abstract classes
# But we have a module name "ABC" for this

from abc import ABC, abstractmethod

# for "Declaration" Just use "Pass"
# Abstract Method -> A method only having decalaration no body, is abstract method 
# Abstract Class -> A class having abstract methods is k/a abstract class


# pass ABC as inheritance to the abstract class and use decorator
class Computer(ABC):
    @abstractmethod
    def process(self):
       pass

# Notice, if we don't use ABC and @asbtractmethod decorator, can create an object 
# c1=Computer()   ->  # can't make an object since this class is abstract

class Laptop(Computer):
    def process(self):
        print("running")

l1=Laptop()
l1.process()       # see had used abstract class and implemented the fuction -> its running

# Abstact class has at least one abstract method, 
# need to implement all the abstract methods
