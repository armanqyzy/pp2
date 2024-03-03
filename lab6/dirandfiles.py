
"""
1. Write a Python program to list only directories, 
files and all directories, files in a specified path. 
"""
import os

path = r"C:\Users\Dias\Desktop"

entries = os.listdir(path)

print("Directories:")
for entry in entries:
    full_path = os.path.join(path, entry)
    if os.path.isdir(full_path):
        print(entry)

print()
print("Files:")
for entry in entries:
    full_path = os.path.join(path, entry)
    if os.path.isfile(full_path):
        print(entry)

print()
print("All Directories and Files:")
for entry in entries:
    full_path = os.path.join(path, entry)
    if os.path.isdir(full_path):
        print(f"[Directories] {entry}")
    else:
        print(f"[Files] {entry}")

"""
2. Write a Python program to check for access 
to a specified path. Test the existence, readability, 
writability and executability of the specified path
"""
import os

path = r"C:\Users\Dias\Desktop\pp1\pp2\lab5\well.txt"

if not os.path.exists(path):
    print("Does not exist")
else:
    if os.access(path, os.R_OK):
        print("Path is readable.")
    else:
        print("Path is not readable.")
    
    if os.access(path, os.W_OK):
        print("Path is writable.")
    else:
        print("Path is not writable.")
    
    if os.access(path, os.X_OK):
        print("Path is executable.")
    else:
        print("Path is not executable.")



"""
3. Write a Python program to test whether a 
given path exists or not. If the path exist 
find the filename and directory portion of the given path. 
"""
import os

path = r"C:\Users\Dias\Desktop"

if os.path.exists(path):
    directory = os.path.dirname(path)
    filename = os.path.basename(path)
    
    print(f"Path exists at {path}")
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
else:
    print(f"Path {path} does not exist")

"""
4. Write a Python program to count the 
number of lines in a text file.
"""

def num_counter(path):
    line_count=0
    with open(path, 'r') as file:
        for line in file:
            line_count += 1
    print("Number of lines in the file: ", line_count)

path = "well.txt"
num_counter(path)


"""
5. Write a Python program to write a list to a file.
"""
mylist = ['apple', 'banana', 'orange']

with open('well.txt', 'w') as file:
    for item in mylist:
        file.write("%s\n" % item)

res = open('well.txt')
print(res.read())



"""
6. Write a Python program to generate 
26 text files named A.txt, B.txt, and so on up to Z.txt
"""
import string
import os

alphabet = string.ascii_uppercase

for letter in alphabet:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

files = os.listdir()

for file_name in files:
    with open(file_name, "w") as f:
        pass


"""
7. Write a Python program to copy 
the contents of a file to another file  
"""
from shutil import copyfile
copyfile('no.txt', 'well.txt')


"""
8. Write a Python program to delete 
file by specified path. Before deleting 
check for access and whether a given path exists or not.
"""
import os
path = r"C:\Users\Dias\Desktop\pp1\pp2\lab6\no.txt"

if os.path.exists(path):
    os.remove(path)
else:
    print(f"Path {path} doesnt exist!!!")