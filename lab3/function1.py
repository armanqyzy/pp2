"""
1)
   A recipe you are reading states how many grams you need for the ingredient. 
     Unfortunately, your store only sells items in ounces.
  Create a function to convert grams to ounces.
     ounces = 28.3495231 * grams
"""
def converter(g):
    ounces = g * 28.3495231 
    return ounces

gram=float(input())
s=converter(gram)
print(s)

"""
2) 
 Read in a Fahrenheit temperature. 
 Calculate and display the equivalent centigrade temperature.
 The following formula is used for the conversion:
       C = (5 / 9) * (F - 32)


"""
def temp(F):
    C = (5 / 9) * (F - 32)
    print(C)

t_f=float(input())
temp(t_f)

"""
3)
Write a program to solve a classic puzzle:
 We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
 How many rabbits and how many chickens do we have? create function:
      solve(numheads, numlegs):

"""
numheads = int(input())
numlegs = int(input())

def solve(numheads, numlegs):

# x + y  = 35 (humheads) | *2
# 2x + 4y = 94 (numlegs)

# -2y = -24
# y = 12
# x = numheads - y
# x = (numlegs-4y)/2
# 2numheads - 2y = numlegs - 4y
# 2y = numlegs - 2numheads
    y = (numlegs - 2*numheads)/2
    x = numheads -y
    
    print(f"Chickens: {x}, Rabbits: {y}")


"""
4)
You are given list of numbers separated by spaces.
Write a function filter which will take
list of numbers as an agrument and returns
only prime numbers from the list.
"""
def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter(num):
    return[n for n in num if isprime(n)]

a = input()
a_list=[int(n) for n in a.split()]

prime=filter(a_list)
print(prime)




"""
5)  
    Write a function that accepts string
    from user and print all permutations of 
    that string.
"""

from itertools import permutations

def permutat(n):
    all=permutations(n)
    return list(arr)

word=input()
result=permutat(word)

print(result)

"""
6)
Write a function that accepts string from user,
 return a sentence with the words reversed. 

 We are ready -> ready are We
"""
def reverse(i):
    s=''
    i=i[-1::-1]
    for j in i:
        s=s+j+''
    print(s)
w=input()
rev=reverse(w)
print(rev)
"""
7)
Given a list of ints, 
return True if the array contains
 a 3 next to a 3 somewhere.

 def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False

"""
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

li=input()
a_l=[int(nums) for nums in li.split()]
result=has_33(a_l)
print (result)
"""
8)
Write a function that takes in a list of integers 
and returns True if it contains 007 in order

def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False

"""
def spy_game(nums):
    for i in range(len(nums)):
        if(nums[i]==0):
            for j in range(i, len(nums)-1):
                if nums[j]==0:
                    for g in range(j, len(nums)):
                        if nums[g]==7:
                            return True
    return False


"""
9)
Write a function that computes
 the volume of a sphere given its radius.

"""
def volume(sphere):
    return (4/3)*3.14*(r**3)
r=float(input())
result=volume(r)
print(result)

"""
10)
Write a Python function that takes a list and 
returns a new list with unique unique of the first list. 

Note: don't use collection set.
"""
def removing(n):
    unique = []
    for element in n:
        if element not in unique:
            unique.append(element)
    return unique

a=input()
l=[int(n) for n in a.split()]
r=removing(l)
print(r)

"""
11)
Write a Python function that checks
whether a word or phrase is palindrome or not.
 
   Note: A palindrome is word, phrase, or sequence
   that reads the same backward as forward, e.g., madam


"""
def ispalindrome(s):
    if s==s[-1::-1]:
        return True
    return False

a=input()
r=ispalindrome(a)
print(r)
"""
12)
Define a functino histogram() that takes a list
 of integers and prints a histogram to the screen.
 
  For example, histogram([4, 9, 7]) should print the following:

****
*********
*******

"""
def histogram(n):
    for i in n:
        print("*"*i)
a=input()
l=[int(n) for n in a.split()]
r=histogram(l)
print(r)


"""
13)
Write a program able to play the "Guess the number" - game,
where the number to be guessed is randomly chosen
between 1 and 20. This is how it should work when run in a terminal:

Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""
import random

def guess_number():
    print("Hello! What is your name?")
    player_name = input()
    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    target_number = random.randint(1, 20)
    attempts = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess > target_number:
            print("Your guess is too high.")
        elif guess < target_number:
            print("Your guess is too low.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {attempts} guesses!")
            break

guess_number()
