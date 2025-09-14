#1.1
print("It's alright")
print("He is called 'op'")
print('He is called "bop"')

#1.2
a = """alooooooooooooo""" # or '''
print(a)
#2.1
b = "Hello, World!"
print(b[2:5])
#2.2
b = "Hello, World!"
print(b[:5])
#2.3
b = "Hello, World!"
print(b[2:])
#2.4
b = "Hello, World!"
print(b[-5:-2])
#3.1
a = "Hello, World!"
print(a.upper())
#3.2
a = "Hello, World!"
print(a.lower())
#3.3
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#3.4
a = "Hello, World!"
print(a.replace("H", "J"))
#3.5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#4.1
a = "Hello"
b = "World"
c = a + b
print(c)

#4.2
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#5.1
age = 18
txt = f"My name is di, I am {age} years old"
print(txt)
#5.2
txt = f"The price is {10 * 5} dollars"
print(txt)

#6
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

#7.1
a="hello"
b=a.isalpha()
print(b)
#7.2

a="1223"
b=a.isdigit()
print(b)