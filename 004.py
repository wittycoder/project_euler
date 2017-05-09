max_prod = 0

for x in range(0, 1000):
  for y in range(0, 1000):
    prod = x * y
    if prod > max_prod:
      # Check result for palendrome
      if str(prod) == str(prod)[::-1]:
        max_prod = prod
        
print(max_prod)