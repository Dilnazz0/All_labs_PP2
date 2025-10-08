def Div():
    n=int(input("enter the number:"))
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i

a=Div()
for i in a:
    print(i)