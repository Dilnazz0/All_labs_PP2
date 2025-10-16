import re
s=input("enter:")
result=re.sub(r"([A-Z][a-z]+)",r" \1 ",s).strip()
print(result)