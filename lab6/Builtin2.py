a=input("Enter a string:")
u=0
l=0
for i in a:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print("Number of uppercase letters:",u,"Number of lowercase letters:",l)