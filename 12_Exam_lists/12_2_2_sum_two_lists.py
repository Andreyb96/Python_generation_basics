from itertools import zip_longest

s1 = input()
l = [int(i) for i in s1.split()]

s2 = input()
m = [int(i) for i in s2.split()]

print(*[sum(i) for i in zip_longest(l, m, fillvalue=0)])