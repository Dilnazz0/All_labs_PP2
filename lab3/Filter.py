class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers
        
    def Numbers(self):
        self.numbers=list(map(int, input("Enter numbers separated by space: ").split()))
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def filter_primes(self):
        primes = list(filter(lambda x: self.is_prime(x), self.numbers))
        return primes
    

obj = PrimeFilter()
obj.Numbers()

print("Prime numbers in the list:", obj.filter_primes())


