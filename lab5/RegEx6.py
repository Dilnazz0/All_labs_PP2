import re
s=input("enter:")
result=re.sub(r"[ , .]",":",s)
print(result)