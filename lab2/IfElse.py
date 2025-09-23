#1
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#2
#One line if statement:

if a > b: print("a is greater than b")

#One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")
#One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#And,or,not
a = 200
b = 33
c = 500
if a > b and c > a :
  if a > b or a > c:
    if not a > b:
     print("Both conditions are True")#or something else

#Nested If
#You can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#чтобы избежать ошибки pass
a = 33
b = 200

if b > a:
  pass
