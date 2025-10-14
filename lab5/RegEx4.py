import re
s=input("enter a sequence:")
result=re.findall(r"[A-Z][a-z]+",s)
print(result)