# decorators ek function hai, jo dusre fucntion ko change krke return krta hai

def salutation(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx()
        print("Thanks for using")
    
    return mfx


@salutation
def greet():
    print("hello Guest")

# if agar hm chahate, hai ki hello krne se phle 
# "good morning" print kre 
# and end me "Thnaks for using" print kre

# Problem in Modification : if we have 100 or 1000 or similar functions to modify

# decorator takes a function in input and return a function(k/a modified funciotn) as output

greet()

print('------------------------other way to call------------------------------------')
# using decorator is similar to call a new modified function using decorator name
salutation(greet())



# What if the function passed to the decatorator function has arguments
# use *args and **kwargs in the arguments of decorator function