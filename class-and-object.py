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

#--------------------------------Git Concepts Doubts Clearing---------------------------------------------------------------------
# Git pull error 
# Flow : 
# 1) created a new repo with a readme file on remote
# 2) created local files, add them to git, had made a commit, and then trying to push
# 3) git pull error
# WHY ERROR ? -> bcoz. local has new commit and remote also has other commit that are not common

# Previously What i Do ?
# To bypass this, I firstly do everytime : "Git Pull" before adding any files or commiting my changes
# This is why previously git pull don't give any error

# How to overcome if error comes on git pull for 'divergent commits histories'
# do : "git pull origin main --rebase"
# what it means -> 
# it means after it will pull all the changes to your local and will do rebasing
# implying that first it will pull the file and add the readme.txt commit to your local git 
# then it will add the new commit(for local file changes) on top of it(Rebasing) 

# if you do git log, it will have 2 commits instead of one 

#------------------------------------------------------------------------------------------------------------------------------------------------------
# Why set 'Upstream in Git'
# "upstream" refers to the remote branch that your local branch is tracking 
# — basically, the branch you’ll pull from and push to by default.

# "git pull" need to know : Pull from where? Which remote? Which branch?
# Syntax : 'git pull <remote branch>
# Thus, git pull and git push will not work, they need to specify the branch name

# command to set upstream : "git branch --set-upstream-to=origin/main main"
# a simple way to do so : Using '-u' flag
# git push -u origin main
