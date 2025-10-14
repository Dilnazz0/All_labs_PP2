import re
s=input("enter:")
result=re.findall(r"[A-Z][a-z]+",s)
print(result)