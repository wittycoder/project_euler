num = 1

while True:
  for i in list(range(2, 21))[::-1]:
    if num % i == 0:
      #print('0 for num,i: ', num, i)
      continue
    else:
      #print('breaking loop for ', num, i)
      break
  else:
    print('Found number: ', num)
    break

  num += 1