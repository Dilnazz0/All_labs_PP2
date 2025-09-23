#1
print(10>7)
print(10==4)
print(10<8)

#2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#3
print(bool("hi"))
print(bool(18))

#4
x="helloooo"
y=21
print(bool(x))
print(bool(y))

#5
print(bool("abc"))
print(bool(12345678))
print(bool(["apple","qiwi","strawberry"]))

#6
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#8
def myFunction():
  return True
print(myFunction())

#9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#10
x=570
print(isinstance(x,int))