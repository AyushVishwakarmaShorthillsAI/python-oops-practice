
def greet():
    print("Hello User, Have a nice day from Ayush :) ")

# How to avoid this ?
# use if __name__=="__main__"

if __name__=="__main__":
    greet()

# what aboves does : " agar is function ko isi file se run kiya ja rha hai"
# -> "To usko chalaoo,  agar is function ko dusre file se run kiya ja rha hai to na chalaoo"

# if __name__=="__main__"
# determines wheter the script is being run directly or being imported