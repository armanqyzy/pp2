"""
1. Write a Python program that matches 
a string that has an `'a'` followed by 
zero or more `'b'`'s.
"""
import re
with open("row.txt", "r", encoding="utf-8") as file:
    text=file.read()
def fstr(s):
    finding=re.findall(r'ab*', s)
    if finding:
        print(True)
    else:
        print(False)
s=input()
fstr(s)


"""
2. Write a Python program that matches 
a string that has an `'a'` followed by 
two to three `'b'`.
"""
import re
with open("row.txt", "r", encoding="utf-8") as file:
    text=file.read()
def fstr(s):
    finding=re.search(r'ab{2}|b{3}', s)
    if finding:
        print(True)
    else:
        print(False)
s=input()
fstr(s)


"""
3. Write a Python program to 
find sequences of lowercase letters 
joined with a underscore.
"""

import re
with open("row.txt", "r", encoding="utf-8") as file:
    text=file.read()
def fstr(s):
    finding='^[a-z]+_[a-z]+$'
    if re.search(finding, s):
        print(True)
    else:
        print(False)
s=input()
fstr(s)


"""
4. Write a Python program to find 
the sequences of one upper case letter 
followed by lower case letters.
"""
import re
with open("row.txt", "r", encoding="utf-8") as file:
    text=file.read()
def fstr(s):
    finding='[A-Z]{1}+[a-z]'
    if re.search(finding, s):
        print(True)
    else:
        print(False)
s=input()
fstr(s)



"""
5. Write a Python program that matches 
a string that has an `'a'` followed by 
anything, ending in `'b'`.
"""
import re
with open("row.txt", "r", encoding="utf-8") as file:
    text=file.read()
def fstr(s):
    finding='a*+b$'
    if re.search(finding, s):
        print(True)
    else:
        print(False)
s=input()
fstr(s)


"""
6. Write a Python program to replace 
all occurrences of space, comma, or 
dot with a colon.
"""
import re
with open("row.txt", "r", encoding="utf-8") as file:
    text=file.read()
def fstr(s):
    s=re.sub("[ ,.]", ':', s)
    print(s)
s=input()
fstr(s)


"""
7. Write a python program to 
convert snake case string to 
camel case string.
"""
import re
with open("row.txt", "r", encoding="utf-8") as file:
    text=file.read()
def fstr(s):
    print(''.join(x.capitalize() or '_' for x in s.split('_')))
s=input()
fstr(s)


"""
8. Write a Python program 
to split a string at uppercase letters.
"""
import re
with open("row.txt", "r", encoding="utf-8") as file:
    text=file.read()
def fstr(s):
    s=re.split("[A-Z]", s)
    print(s)
s=input()
fstr(s)


"""
9. Write a Python program to 
insert spaces between words 
starting with capital letters.
"""
import re
with open("row.txt", "r", encoding="utf-8") as file:
    text=file.read()
def fstr(s):
    s=re.sub(r"(\w)([A-Z])", r"\1\2", s)
    print(s)
s=input()
fstr(s)


"""
10. Write a Python program to 
convert a given camel case string to snake case.
"""
import re
with open("row.txt", "r", encoding="utf-8") as file:
    text=file.read()
def fstr(s):
    s=re.sub('(.)([A-Z][a-z])+', r'1\_\2', s)
    print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower())
s=input()
fstr(s)
