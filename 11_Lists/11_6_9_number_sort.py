l = [int(i) for i in input().split()]
l.sort()

print(*l)
print(*l[::-1])