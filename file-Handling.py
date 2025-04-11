# for permanent storage files are used 

# to open a file
f = open('./files/example.txt', 'r')   # r => read mode
print(f)    # we had fetched the data, the metadata

print(f.read())  # prints the whole doc

print(
    '-------------------------------------------------------------------------------'
)

# readline() to read a single line

# writing data

f2=open('./files/new.txt', 'w')   # w => write
f2.write('Something that i wrote in the new file')
# how to append
# using the 'w' => delete all and write something new
# for appending open a file with 'a' mode
f3=open('./files/new.txt', 'a')
f3.write('\nappended data')
f3.write('\n ------------------------------------------------------')

#copying all the data of file 'example.txt' to 'new.txt'


# copying will not happen if you do it normally without using below
f.seek(0)  # Moves the file pointer back to the beginning

for data in f:
    f3.write(data)

# NOTE : actually the file object 'f', 'f2', 'f3' are poiinters to a characters, that get exhausted
# after you used then 
# readline -> send the pionter to end of first line 
# read -> send the pointer to end of the doc
# similar for others