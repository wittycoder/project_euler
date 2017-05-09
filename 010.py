from functools import reduce

from fast_prime import primes

print(reduce(lambda x, y: x + y, primes(2000000)))