# Dunder methods (short for double underscore methods) in Python are special methods 
# that have double underscores before and after their names, like __init__, __str__, __len__, etc. 
# These methods are also known as magic methods or special methods and they enable the customization of class behavior.

# we had covered mostly in opearator overloading and some left here

# Note : use case of __str__ is while printing 
# in str can only return and not print 
class Dark_Soul:

    def __init__(self, name):
        print('Arised from the hells to strenthen people endulging in fear')
        self.name=name

    
    def __str__(self):
        return (f'You are taking to the {self.name}, be Careful !!')
    

class Divine_Soul:
    def __init__(self, name):
        print('Uplifted one, no grudges and enemies ')
        self.name=name

    def __str__(self):
        return (f'You are talking to the {self.name}, Keep flurshing ***')

dark_s1=Dark_Soul('Akahatein')
div_s1=Divine_Soul('Phegasis')

print(dark_s1)
print(div_s1)


# ---------------------------------------------------------------------------------------
# use case of __len__ and __repr__
class train:
    def __init__(self, name, speed):
        print(f'You are currently sitting in {name} travelling with an avg speed of {speed} km/hr')
        self.name = name
        self.speed = speed

    def photo(self, pic):
        self.img = pic

    # def __str__(self):
    #     return self.img
    
    def __repr__(self):
        return "This is the callback for str, This should return a photo of the train Name {self.name}"

    def __len__(self):
        return self.speed

bullet_train = train('Bullet Train', 250)
bullet_pic = r"""
     ________________________
 ___||__________________||___\
|___    Fast Express     ___|
    o-o--o-o--o-o--o-o--o
"""

bullet_train.photo(bullet_pic)
print(bullet_train)
print(f"the length of {bullet_train.name} is : {len(bullet_train)}")



freight_train = train('Freight Train', 120)
freight_pic = r"""
      _____      _____      _____
 ____|__|__|____|__|__|____|__|__|___
|                          Cargo     |
|___________________________________|
  (o)                      (o)   (o)
"""

freight_train.photo(freight_pic)
print(freight_train)
print(f"the length of {freight_train.name} is : {len(freight_train)}")

