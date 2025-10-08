import math
n=int(input("enter number of sides:")) 
l=int(input("enter the length of a side:"))
a=(n*l**2)/4*math.tan(math.pi/n)
print("The area of the polygon is",math.ceil(a) )