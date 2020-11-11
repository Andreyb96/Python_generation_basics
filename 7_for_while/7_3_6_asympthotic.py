from math import *

n = int(input())

l = [1/i for i in range(1,n+1)]
print(sum(l) - log(n))