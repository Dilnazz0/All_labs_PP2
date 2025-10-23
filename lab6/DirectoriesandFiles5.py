import os
l=input("enter a list elements:").split()
a=list(l)
p=input("enter a path:")
with open(p,'w')as f:
    for i in l:
        f.write(i+'\n')
print("list elements written to the file successfully")