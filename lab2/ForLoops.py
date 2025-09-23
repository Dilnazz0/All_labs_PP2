#Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#Loop through the letters in the word "banana":

for x in "banana":
  print(x)

#break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#continue


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#range() function
for x in range(6):
  print(x)

#Using the start parameter:

for x in range(2, 6):
  print(x)
#1 2+3 step 5+3 
for x in range(2, 30, 3):
  print(x)
#else
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#break #If the loop breaks, the else block is not executed.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested Loops
#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#pass чтобы не было ошибки
for x in [0, 1, 2]:
  pass
