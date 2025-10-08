def Squares():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    for i in range(a,b+1):
        yield i*i
s=Squares()
for i in s:
    print(i)