# this method sucks, takes over 30 hours to run on machine!!!


from functools import reduce
from fast_prime import primes, is_prime

import time

start = time.time()

p = primes(1000000)
#p = primes(100000)
long_num = 0
long_sum = 0

print('prime time = ', time.time() - start)

start = time.time()
for x in p[::-1]:
    for i in range(len(p)):
        sum_list = []
        sum = 0
        count = i
        while sum < x:
            sum_list.append(p[count])
            #print(sum_list)
            sum = reduce(lambda x,y: x+y, sum_list)
            if sum == x:
                if len(sum_list) > long_sum:
                    long_sum = len(sum_list)
                    long_num = x
            count += 1

print('consecutive sum of primes took ', time.time() - start)
print(long_sum)
print(long_num)
