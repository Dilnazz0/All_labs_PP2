import math
r=float(input("Enter the radius:"))
def Volume(rad):
    return ((4/3)*math.pi*r**3)
print(f"Volume of sphere with radius {r} is {Volume(r)}")