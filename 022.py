
def sum_name(n):
    sum = 0
    for c in n:
        sum += ord(c) - 64
    return sum

total = 0

names = []
with open('p022_names.txt', 'r') as f:
    for i in f.readline().split(','):
        names.append(i.split('"')[1])


for idx, name in enumerate(sorted(names)):
    #if name == 'COLIN':
    #    print(idx+1)
    total += sum_name(name) * (idx + 1)

print(total)
