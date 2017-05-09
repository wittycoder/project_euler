low=1
high=100

square_sum = 0
sum = 0
for i in range(low, high+1):
  square_sum += i**2
  sum += i

print(sum**2 - square_sum)