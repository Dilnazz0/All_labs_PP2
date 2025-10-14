import re
s=str(input("enter a string:"))
result=re.fullmatch(r"ab{2,3}",s)
print(result)