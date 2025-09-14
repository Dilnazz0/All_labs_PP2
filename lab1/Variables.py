#1
x = 7
y = "Dilnaz"
print(x)
print(y)

#2
x = 7
x = "soap"
print(x)

#3
x = str(1)
y = int(2)
z = float(3)
print(x)
print(y)
print(z)

#4
x = 7
y = "Dilnaz"
print(type(x))
print(type(y))

#5
x = "Dilnaz"
y = 'Dilnaz'
print(x)
print(y)

#6
d = 4
D = "Dilnaz"
print(d)
print(D)

#7
myvar = "Di"
my_var = "Di"
_my_var = "Di"
myVar = "Di"
MYVAR = "Di"
myvar2 = "Di"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#8.1
x, y, z = "Orange", "Watermelon", "Cherry"
print(x)
print(y)
print(z)

#8.2
x = y = z = "Apple"
print(x)
print(y)
print(z)

#8.3
fruits = ["apple", "orange", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#9.1
x = "Python is perfect"
print(x)

#9.2
x = "Python"
y = "is"
z = "good"
print(x, y, z)

#9.3
x = "Python "
y = "is "
z = "bad"
print(x + y + z)

#9.4
x = 5
y = 10
print(x + y)


#9.5
x = 5
y = "Di"
print(x, y)

#10.1
x="good"

def myfunc():
    print("python is" " " + x)

myfunc()

#10.2
x="good"

def myfunc():
    x="snake"
    print("python is" " " + x)

myfunc()

print("python is" " " + x)

#10.3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#10.4
x = "good"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)