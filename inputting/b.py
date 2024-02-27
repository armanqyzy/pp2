#seperate string
x=input()
for i in x:
    print(i)
#seperate string #2 in list
x=input()
y=list(x)
print(y)
#if seperate sentence to multiple words
x=input()
y=x.split()
print(y)
#get the length:
x=input()
y=len(x)
print(y)
#word in text
x=input()
if "Hello" in x: #u can use "not"
    print("Yes")
else:
    print("No")
#slicing
x=input()
print(x[1:5])

#last index and letter
x=input()
ind = len(x) - 1
letter = x[ind]
print(letter)

#upper 1st letter
txt = "hello welcome"
x = txt.capitalize()
print (x)

#lower 1st letter
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#find
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#change list
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#change and add
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#add the end of list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove from tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

