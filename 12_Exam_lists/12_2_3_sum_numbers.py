l = [i for i in input().split()]
s = '+'.join(l)
s += '=' + str(sum([int(i) for i in l]))
print(s)