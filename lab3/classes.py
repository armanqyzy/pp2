"""
1)
Define a class which has at least two methods:
 getString: 
     to get a string from console input
printString: 
     to print the string in upper case.
"""
class two_classes():
    def getString(n):
        n.name = input()
    def printString(n):
        print(n.name.upper())
hola = twoclasses()
hola.getString()
hola.printString()

"""
2)
Define a class named Shape and its subclass Square.
The Square class has an init function
which takes a length as argument. 

 Both classes have a area function 
 which can print the area of the shape where 
 Shape's area is 0 by default.
"""
class Shape():
    def __init__(n):
        n.Area=0
class Square(Shape):
    def __init__(n):
        n.length=int(input())
        n.Area=n.length*n.length
        n.area()
    def area(n):
        print(n.Area)
ex = Square()

"""
3)
Define a class named Rectangle which inherits 
from Shape class from task 2. Class instance can be 
constructed by a length and width. 
The Rectangle class has a method which 
can compute the area.
"""
class Shape():
    def area(self):
        self.Area=0
class Square(Shape):
    def __init__(self):
        self.length=int(input())
        self.Area=self.length*self.length
        self.area()
    def area(self):
        print(self.Area)
class Rectangle(Shape):
    def __init__(self):
        self.length=int(input())
        self.width=int(input())
        self.Area=self.length*self.width
        self.area()
    def area(self):
        print(self.Area)

ex = Rectangle()



"""
4)
Write the definition of a Point class. 
Objects from this class should have a:

1)a method show to display the coordinates of the point
2)a method move to change these coordinates
3)a method dist that computes the distance between 2 points
"""
import math
class Point():
    def __init__(self):
        self.x1=int(input())
        self.y1=int(input())
        self.x2=int(input())
        self.y2=int(input())
        self.point_coordinates={self.x1:self.y1,}
        self.show()
        self.move()
        self.dist()
    def show(self):
        print(self.point_coordinates)
    def move(self):
        self.point_coordinates={self.x2:self.y2,}
    def dist(self):
        self.distance=math.sqrt(pow((self.x2-self.x1), 2)+pow((self.y2-self.y1), 2))
        print(self.distance)
ex = Point()

"""
5)
Create a bank account class that has attributes owner, 
balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.

class Account:
    pass
"""
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance is ${self.balance}"
        else:
            return "Invalid deposit amount."
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew ${amount}. New balance is ${self.balance}"
            else:
                return "You're poor, you have no money"
        else:
            return "Invalid withdrawal amount."
    def get_balance(self):
        return f"Account balance for {self.owner}: ${self.balance}"

owner_name = input("What is you're name? ")
initial_balance = float(input("The initial balance: "))
my_account = Account(owner_name, initial_balance)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("What you wanna see? (1/2/3/4): ")

    if choice == "1":
        amount = float(input("The deposit amount: "))
        print(my_account.deposit(amount))
    elif choice == "2":
        amount = float(input("The withdrawal amount: "))
        print(my_account.withdraw(amount))
    elif choice == "3":
        print(my_account.get_balance())
    elif choice == "4":
        print("Exiting your account.")
        break


"""
6)
Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
"""
class Prime_Numbers:
    def __init__(self,n):
        self.n = n
    def is_prime(self, n):
        if (n>1):
            for i in range(2,n):
                if (n%i==0):
                    return False
            return True
        return False
    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x),self.n))
    
arr = input()
n = list(map(int, arr.split()))
prime_filter = Prime_Numbers(n)
print(prime_filter.filter_primes())