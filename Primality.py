# check if a number if a prime number
import math
def prime(num):
    # iterate only up through the square root of num
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True

# generating a list of prime
# return number of prime that strictly less than n
def countPrime(n):
    count = 0
    # 0 and 1 is not a prime number
    prime = [0, 0] + [1] * (n-2)
    for i in range(2, n):
        if prime[i]:
            count += 1
            for j in range(i, n, i):
                prime[j] = 0
    return count


# test case
print(prime(25))
print(prime(7))
print(prime(41))

print(countPrime(10))
