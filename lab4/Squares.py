def Square():
    n=int(input("enter the some number:"))
    for i in range(1, n+1):
        yield i*i

a=Square()
for i in a:
    print(i)