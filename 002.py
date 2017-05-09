def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)

sum = 0

for index, fib_num in enumerate(fib()):
    if fib_num % 2 == 0:
	    sum += fib_num
		
    if fib_num >= 4000000:
	    break

print sum