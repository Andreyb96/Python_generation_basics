n = int(input())

height = n//2 + 1

for i in range(1,n+1):
    if (i <= n//2 + 1):
        print('*' * i)
    else:
        print('*' * (n-i+1))