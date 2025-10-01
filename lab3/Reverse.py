def reverse(strings):
    strings=list(strings.split())
    strings.reverse()
    for i in strings:
        print(i, end=" ")

k=str(input("enter the sentence separated by space:"))
reverse(k)