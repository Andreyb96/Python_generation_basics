s = input()
l1 = s.split(' ')
l = [int(i) for i in l1]
maxIdx = l.index(max(l))
max = max(l)
minIdx = l.index(min(l))
min = min(l)

l[maxIdx] = min
l[minIdx] = max

print(*l)