
# 9) Prime time (4 ქულა)

# Write a function that takes a 
# maximum bound and returns all primes 
# up to and including the maximum bound.

# For example:
# 11 => [2, 3, 5, 7, 11]

def prime_time(num) : 
    if num < 2:
        return "error! 2 isn't prime."
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime(max_prime) :
    prime_nums = [] 
    for num in range(2, max_prime + 1):
        if prime_time(num):
            prime_nums.append(num)
    return prime_nums


print(prime(20))
    