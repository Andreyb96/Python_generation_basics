n = int(input())

for i in range(1, n+1):
    l = [str(j) for j in range(1, i)]
    l.extend([str(j) for j in range(i, 0, -1)])
    print(''.join(l))