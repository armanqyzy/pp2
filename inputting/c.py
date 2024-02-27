#dublicates
x=["1", "2", "2", "1", "3"]
y=list(set(x))
print(y)

#2nd way
x=["1", "2", "2", "1", "3"]
uni=[]
for z in x:
    if z not in uni:
        uni.append(z)
print(uni)



#christmas tree
def christmas_tree(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

m=int(input("input for christmas tree "))
christmas_tree(m)

#обратная cristmas tree
def ct(n):
    for i in reversed(range(n)):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
x=int(input("reversed tree "))
y=ct(x)
print(y)

#palindrom
s = input("cheking word palindrom ")
if s == s[::-1]:
    print("YES!")
else:
    print("ew no")

#prime
x=[1, 2, 3, 5, 7, 8]
def isprime(n):
    if n < 2:
        return False
    for i in range(2, int (n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
def filter(num):
    return[n for n in num if isprime(n)]

prime=filter(x)
print(prime)


#reverse string sentence
def reverse(sentence):
    words=sentence.split()
    return ' '.join(words[::-1])
x=input('enter sentence reverse ')
y=reverse(x)
print(y)


#square without inner filler
def square(n):
    print('*' * n)
    for i in range(n - 2):
        print('*' + ' ' * (n - 2) + '*')
    print('*' * n)
x = int(input())
y=square(x)
print(y)

class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printing(self):
        print(f"Name: {self.name}, Age {self.age}, Gender: {self.gender}")

p1=Person("Anara", 18, "F")
p1.printing()

#adding subclass
class Student(Person):
    def __init__(self, name, age, gender, id):
        super().__init__(name, age, gender)
        self.id=id

    def printing(self):
        super().printing()
        print(f"ID: {self.id}")
p1=Student("Bob", 25, "M", "23BD")
p1.printing()


class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
    def printing(self):
        print(f"Well your name is {self.name}, {self.surname}, and u are {self.age}.")

class Coursee(Person):
    def __init__(self, name, surname, age, course_n):
        super().__init__(name, surname, age)
        self.course_n=course_n
    def printing(self):
        super().printing()
        print(f"Well course is {self.course_n}.")
p1=Coursee("Anna", "Bolein", "18", "2")
p1.printing()
    

#крест христианский
def draw_cross(n):
    for i in range(n):
        for j in range(n):
            if i == n // 2 or j == n // 2:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

draw_cross(5)

# крест Х
def draw_cross(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == n - 1 - j:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

draw_cross(5)


x=[1,2,3,4,5,6,7,8]
for y in x:
    print(y)
