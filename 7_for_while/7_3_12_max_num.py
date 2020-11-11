n = int(input())

l = [int(input()) for i in range(n)]

print(max(l))
l.remove(max(l))
print(max(l))