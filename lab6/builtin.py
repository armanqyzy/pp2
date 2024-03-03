"""
1. Write a Python program with builtin function to multiply all the numbers in a list
"""

from functools import reduce

def multiplying(n):
    return reduce(lambda x, y: x*y, n)



liist=[12,3,4,5,6,7,8,9,10]
res=multiplying(liist)
print(res)


"""
2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
"""

def counter(s):
    up=0
    low=0
    for char in s:
        if char.isupper():
            up+=1
        elif char.islower():
            low+=1
    return up, low


stringg=input()
first, second=counter(stringg)
print(f"{first},and lower is: {second}")



"""
3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.
"""


def ispalindrome(s):
    if s==''.join(reversed(s)):
        return "YES"
    else:
        return "NO"



s=input()
res=ispalindrome(s)
print(res)


"""
4. Write a Python program that invoke square root function after specific milliseconds. 
    ```
    Sample Input:
    25100
    2123
    Sample Output:
    Square root of 25100 after 2123 miliseconds is 158.42979517754858
    ````
"""

import time
import math

n=int(input())
milisec=int(input())

time.sleep(milisec/1000.0)
x=math.sqrt(n)

print(f"Sqare root of {n} after {milisec} miliseconds is {x}")


"""
5. Write a Python program with builtin function that returns True if all elements of the tuple are true.
"""

def tuptrue(mine):
    if all(mine):
        return True
    else:
        return False

mytuple=(1,2,3,4,5,6,7,8,9,10)
print(tuptrue(mytuple))