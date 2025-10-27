import random
import string
# pwd_length is the number of characters the user wishes to generate for their
# password. As such, it must be converted from a string to an integer.

pwd_length = int(input("Enter the number of characters to be generated "))
print(pwd_length)


def gen_pwd():
    pwd = ""
    for lower_chars in range(pwd_length):
        pwd += random.choice(string.ascii_lowercase)
        
    return pwd

pwd = gen_pwd()
print(pwd)