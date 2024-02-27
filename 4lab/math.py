"""
Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904
"""
import math

degree=int(input("Input degree: "))
#1 way:
func=round(math.radians(degree), 6)
print(f"1 Output radian: {func}")

# 2nd way:
radian=round(float(degree * (math.pi)/180), 6)
print(f"2 Output radian: {radian}")



print("2:")
"""
Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
"""
import math

hight=int(input("Height: "))
base1=int(input("Base, first value: "))
base2=int(input("Base, second value: "))

area=1/2*hight*(base1+base2)

print(f"Output: {area}")


print("3:")
"""
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""
import math

num=int(input("Input number of sides: "))
lenth=int(input("Input the length of a side: "))

area=int(num*pow(lenth, 2)/math.tan((math.pi)/num)/4)

print(f"The area of the polygon is: {area}")


print("4:")
"""
Write a Python program to calculate the area of a parallelogram.
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
"""
import math

lentgh=int(input("Length of base: "))
hiight=int(input("Height of parallelogram: "))

area=float(lentgh*hiight)

print(f"Output: {area}")