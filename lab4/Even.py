def Even():
    n=int(input("enter the number:"))
    for i in range(0,n+1):
        if i%2==0:
            yield i 

a=Even()
print(",".join(str(i) for i in a))