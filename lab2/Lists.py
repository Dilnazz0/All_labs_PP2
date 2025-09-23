#Python Collections (Arrays)
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

#1
thislist=["a","b","c"]
print(thislist)

#2 Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#3 List Length
thislist=["a","b","c"]
print(len(thislist))

#4 List Items - Data Types, list items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#5 list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]

print(list1)

#6 type()
mylist = ["apple", "banana", "cherry"]

print(type(mylist))

#7 The list() Constructor,using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) 
print(thislist)


#Access items
#1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change Item Value

#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert "watermelon" as the third item:The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add List Items

#append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend() method:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove List Items

#remove() method:удаляет указанный элемент
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#If there are more than one item with the specified value, the remove() method removes the first occurrence:

#pop() method:удаляет по индексу,без индекса последний
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#del keyword ,удаляет по индексу, также может полностью list
#1
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#2
thislist = ["apple", "banana", "cherry"]
del thislist

#clear() method, очищает list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Lists

#for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension

#1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#The Syntax
#Only accept items that are not "apple":


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

#With no if statement:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)

#1
newlist = [x for x in range(10)]

print(newlist)

#2
#Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

#Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]

#Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]

#Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]

#Sort List Alphanumerically
#sort()method

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#чувствителен к регистру,заглавные первее

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#reverse() method
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy Lists,Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#method list(),Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Make a copy of a list with the :(slice) operator:

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Join Lists

#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#List Methods
# Method	         Description
# append()	         Adds an element at the end of the list
# clear()	         Removes all the elements from the list
# copy()	         Returns a copy of the list
# count()	         Returns the number of elements with the specified value
# extend()	         Add the elements of a list (or any iterable), to the end of the current list
# index()	         Returns the index of the first element with the specified value
# insert()	         Adds an element at the specified position
# pop()	             Removes the element at the specified position
# remove()	         Removes the item with the specified value
# reverse()	         Reverses the order of the list
# sort()	         Sorts the list