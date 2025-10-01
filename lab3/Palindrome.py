def Palindrome(word): 
    word=word.lower()
    if word==word[::-1]:
        return("Yes")
    else:
        return("No")
a=input("Enter a word:")
print(Palindrome(a))