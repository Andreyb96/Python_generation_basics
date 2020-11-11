n = int(input())
l = [int(input()) for _ in range(n)]
output = [(x**2 + 2*x + 1) for x in l]
print(*l, sep='\n')
print()
print(*output, sep='\n')