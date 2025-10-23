import os
p = input("Enter a path to file that you want to delete: ")
if os.path.exists(p):
    if os.access(p, os.W_OK):
        os.remove(p)
        print(" File deleted successfully")
    else:
        print("You don't have permission to delete this file")
else:
    print("File doesn't exist")


