#1
#Arithmetic Operators

x=90
y=1

print(x+y) #Addition
print(x-y) #Subtraction
print(x*y) #Multiplication
print(x/y) #Division
print(x%y) #Modulus
print(x**y) #Exponentiation
print(x//y) #Floor division	

#2
#Assignment Operators

#Operator	#Example	       #Same As	
# =	         x = 5	           x = 5	
# +=	     x += 3	           x = x + 3	
# -=	     x -= 3	           x = x - 3	
# *=	     x *= 3	           x = x * 3	
# /=	     x /= 3	           x = x / 3	
# %=	     x %= 3	           x = x % 3	
# //=	     x //= 3	       x = x // 3	
# **=	     x **= 3	       x = x ** 3	
# &=	     x &= 3	           x = x & 3	
# |=	     x |= 3	           x = x | 3	
# ^=	     x ^= 3	           x = x ^ 3	
# >>=	     x >>= 3	       x = x >> 3	
# <<=	     x <<= 3	       x = x << 3	
# :=	     print(x := 3)	   x = 3 print(x)
                               
#3
#Comparison Operators

#Operator	Name	                    Example	
# ==	    Equal	                    x == y	
# !=	    Not equal	                x != y	
# >	        Greater than	            x > y	
# <	        Less than	                x < y	
# >=	    Greater than or equal to	x >= y	
# <=	    Less than or equal to	    x <= y

#4
#Logical Operators

#Operator	Description	                                             Example	
# and 	    Returns True if both statements are true	             x < 5 and  x < 10	
# or	    Returns True if one of the statements is true	         x < 5 or x < 4	
# not	    Reverse the result, returns False if the result is true	 not(x < 5 and x < 10)

#5
#Identity Operators

#Operator	Description	                                              Example	
# is 	    Returns True if both variables are the same object	      x is y	
# is not	Returns True if both variables are not the same object	  x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#6
#Membership Operators

#Operator	Description	                                                                             Example	
# in 	    Returns True if a sequence with the specified value is present in the object	         x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	     x not in y	

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

#7
#Bitwise Operators  

#Operator	    Name	                Description	                                                                                             Example	
# & 	        AND	                    Sets each bit to 1 if both bits are 1	                                                                 x & y	
# |	            OR	                    Sets each bit to 1 if one of two bits is 1	                                                             x | y	
# ^	            XOR	                    Sets each bit to 1 if only one of two bits is 1	                                                         x ^ y	
# ~	            NOT	                    Inverts all the bits	                                                                                 ~x	
# <<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                     x << 2	
# >>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	 x >> 2

#Operator Precedence
#The precedence order
#Operator	                                                    Description	
# ()	                                                        Parentheses	
# **	                                                        Exponentiation	
# (+x , -x , ~x)	                                            Unary plus, unary minus, and bitwise NOT	
# (* , / , // , %)	                                            Multiplication, division, floor division, and modulus	
# (+ , -)	                                                    Addition and subtraction	
# (<< , >>)	                                                    Bitwise left and right shifts	
# &	                                                            Bitwise AND	
# ^	                                                            Bitwise XOR	
# |	                                                            Bitwise OR	
# (== , != , > , >= , < , <= , is , is , not ,  in , not , in)	Comparisons, identity, and membership operators	
# not	                                                        Logical NOT	
# and	                                                        AND	
# or	                                                        OR


#If two operators have the same precedence, the expression is evaluated from left to right.