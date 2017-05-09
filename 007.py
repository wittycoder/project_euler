# python 2.7

import time
s = time.time()

def isprime(x):
    count=0
    for j in range(1, int(x**0.5)+1):
        if (x % j == 0):
            count += 1
            if (count > 1):
                break
    if (count == 1):
        primes.append(i)   
    return
i,primes=2,[]
while True:
    isprime(i)
    if (len(primes) == 10001):
        print (primes[10000])
        break
    i += 1

print time.time() - s   