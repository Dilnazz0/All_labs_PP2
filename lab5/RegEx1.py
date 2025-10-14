import re
s=str(input("enter a string:"))
result=re.fullmatch(r"ab*",s)
print(result)