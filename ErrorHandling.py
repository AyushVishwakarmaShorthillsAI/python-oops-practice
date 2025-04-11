# various error -> mistakes from server, humans, ect.
# programs do not shuts off if a bug/error arise
# whole program do not stops 

# if error comes, then run the code in "Exception block"

# Python uses "TRY-EXCEPT" for this

x=None
x=input("enter a number : ")

#give any character

try :
    for i in range(11):
        print(x**i)
except Exception as e:
    print('invalid input')

# many built in expection  -> Value Error, Index Error, etc.