import os
f=input("Enter a path to 1file:")
s=input("Enter a path to 2file")
with open(f,'r')as a:
    b=a.read()
with open(s,'w')as c:
    c.write(b)
print("File copied successfully")