n = int(input())
l = [input() for _ in range(n)]
k = int(input())
s = ''

for i in range(n):
    st = l[i]
    if len(st)>=k:
        s += st[k-1]

print(s)