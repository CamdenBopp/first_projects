# Version = 0.0.2
# Created Sat Jan 10, 2026 7:42 PM
import platform
import random
import string
import subprocess
# pwd_length is the number of characters the user wishes to generate for their
# password. As such, it must be converted from a string to an integer.
pwd_length = int(input("Enter the number of characters to be generated "))
# Moved the ASCII character set generation logic outside of the for loop to make including toggles for uppercase, lowercase, special symbols and digits easier in future versions.
ASCII_charSet = string.ascii_lowercase + string.ascii_uppercase
# The variable pwd was chosen so as to not conflict with Python's reserved keyword pass

def gen_pwd():
    pwd = ""
    for pwd_Charset in range(pwd_length):
        pwd += random.choice(ASCII_charSet)
    return pwd

pwd = gen_pwd()
print("Generated password: " +pwd)
if platform.system() == "Darwin":
    # Checks if the platform is MacOS so we can use the pbcopy command to copy the generated password to the clipboard.
    subprocess.run("pbcopy", text=True, input=pwd)
