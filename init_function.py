# the init function is a function that is invoked automatically
# each time an object is made
# This do the working to assign value to variable, or simply does work of constructor

class person:
    def __init__(self):
        self.age=18
        self.name='Ayush'
    
    def update(self):
        self.age=21

p1=person()
p2=person()

print(p1.name, p1.age)
print(p2.name, p2.age)
print('above has same data, since init assigns them')

# changing the name and age
p2.name='Rashi'
p2.age=19
print(p1.name, p1.age)
print(p2.name, p2.age)

# WHy self in __init__ also ?
# same answer, any method of class takes an object reference that must be passed to self
# if we don't pass the reference of object in self, then how the method will know which objects to update
# in case of many methods made

p2.update()
p1.update()

print('\nAfter update: ')
print(p1.name, p1.age)
print(p2.name, p2.age)
