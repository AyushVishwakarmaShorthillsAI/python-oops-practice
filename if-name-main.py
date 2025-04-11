# if importing some file(hvaing some functions in it),
# all the functions in the file will get automatically called as soon as imported 

import fileToImport

# see importing above file, directly calls the function in it
# but we just needed the function inside the file not its calling done anywhere

# so, use the if __name__=__main__" in the imported module, so that it do not runs extra times 
# in the module in which its imported 

