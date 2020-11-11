n = int(input())
l = [int(input()) for _ in range(n)]
l.remove(max(l))
l.remove(min(l))
print(*l, sep='\n')