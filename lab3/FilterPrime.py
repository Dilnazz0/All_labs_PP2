def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

def filterprime(numbers):
    return [x for x in numbers if isprime(x)]


n = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Prime numbers:", filterprime(n))
