import re
s=(input("enter a sequence:"))
result=re.findall(r"\b[a-z]+_[a-z]+\b",s)
print(result)