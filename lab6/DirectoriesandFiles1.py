import os
p=input("Enter the path:")
if os.path.exists(p):
    print("\n files and all directories:")
    print(os.listdir(p))
    
    print("\n only directories:")
    for b in os.listdir(p):
        if os.path.isdir(os.path.join(p, b)):
            print(b)
    print("\n only files:")
    for b in os.listdir(p):
        if os.path.isfile(os.path.join(p, b)):
            print(b)
else:
    print("This path does not exist.")

