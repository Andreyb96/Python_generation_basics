l = input().split()
print(*[i[1:] + i[0] + 'ки' for i in l])