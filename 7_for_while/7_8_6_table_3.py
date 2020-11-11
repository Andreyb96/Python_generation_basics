n = int(input())

for i in range(1, n+1):
    for j in range(1, 10):
        print('{0} + {1} = {2}'.format(i, j, i+j))
    print()