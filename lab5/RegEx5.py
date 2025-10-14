import re
s=input("enter a string:")
result=re.fullmatch(r"a.*b",s)
print(result)