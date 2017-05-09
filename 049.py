from fast_prime import primes

p = primes(10000)

nums = []
# find all numbers differing by 3330
for n in p:
    if n < 3330 and (n + 3330) in p:
        nums.append(n)
    elif (n - 3330) in p:
        nums.append(n)

for n in nums:
    if len(str(n)) < 4:
        continue
    chars = [x for x in str(n)]
    if all((c in chars) for c in str(n)):
        if all((c in chars) for c in str(n + 3330)):
            if all((c in chars) for c in str(n + 6660)):
                if n in nums and n + 3330 in nums and n + 6660 in nums:
                    print(n, n + 3330, n + 6660)
