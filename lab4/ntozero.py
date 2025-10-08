def Zero():
    n=int(input("Enter num:"))
    for i in range(n,-1,-1):
        yield i

a=Zero()
for i in a:
    print(i)