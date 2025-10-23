import math
import time
a=int(input("Enter a number:"))
s=int(input("Enter a millisecods:"))
time.sleep(s/1000)
print("Square root of ",a,"after",s,"milliseconds is",math.sqrt(a))