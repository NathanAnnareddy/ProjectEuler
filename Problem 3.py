# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math

def primes(num):
    for i in range(1, math.ceil(math.sqrt(num))):
        if num % i == 0:
            print(i)
    
primes(13195)