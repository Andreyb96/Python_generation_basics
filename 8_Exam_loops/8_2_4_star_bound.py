n = int(input())

for i in range(1, n+1):
    if i==1 or i==n:
        print('*'*19)
    else:
        print('*' + ' ' * 17 + '*')