def square(x):
    return x*x

# lamda equaivalent
sqr=lambda x: x*x
print(sqr(3))

# list comprehension
list1=[1,2,3,4,5,6]
print(list(sqr(x) for x in list1))

# Syntax for list Comprehension : 
# [expression(x) for x in list]

# Note : labda function is nothing just a concise function for better convinience
# and best using with map, filter, or sorted function

# Lambda with sorted :
words=['apple', 'a', 'banana']
sorted_words=sorted(words, key=lambda x:len(x))

# MAP -> Transforms a list
nums=[1,2,3,4,5,6,7,8,9]
new_list=list(map(lambda x: x*2, nums))

# Syntax : map(function, list/iterable)
print(new_list)

# Filter - filter elements based on conditions
even_Nums=list(filter(lambda x:x%2==0, nums))
print(even_Nums)