import os
p=input("Enter a path:")
with open(p,'r')as f:
    a=f.readlines()
    print("Number of lines:",len(a))

