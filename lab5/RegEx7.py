import re
s=input("enter:")
w=re.split(r"_",s)
c=[i.capitalize() for i in w[1:]]
b=w[0]+"" .join(c)
print(b)
