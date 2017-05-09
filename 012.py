from functools import reduce
from divisorGenerator import divisorGenerator


def find_triangles(num=10):
    tri = []
    for i in range(2, 1000000000):
        next_tri = reduce(lambda x,y: x+y, list(range(1, i)))
        tri.append(next_tri)
        if len(tri) == num:
            break
    return tri


for x in find_triangles(20000):
    #print(list(divisorGenerator(x)))
    #print(len(list(divisorGenerator(x))))
    if len(list(divisorGenerator(x))) > 500:
        print(x)
        break
