import os
p=input("Enter a path:")
if os.path.exists(p):
    print(os.path.basename(p))
    print(os.path.dirname(p))