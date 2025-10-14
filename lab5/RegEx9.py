import re
s=input("enter:")
result=re.sub(r"([A-Z])",r"_\1",s).lower()
print(result)