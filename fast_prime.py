def primes(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True
