a = tuple(input("Enter elements for tuple: ").split(' '))
b = list(a)

for i in range(len(b)):
    if b[i].isdigit():
        b[i] = int(b[i])
    elif b[i].lower() == "true":
        b[i] = True
    elif b[i].lower() == "false":
        b[i] = False

print(all(b))


