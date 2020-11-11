m,n = [int(input()) for _ in 'ab']

for i in range(m, n-1, -1):
    if i%2==1:
        print(i)