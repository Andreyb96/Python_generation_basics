n = int(input())
fib = [1, 1]

if (n==1):
    print(1)
elif n==2:
    print('1 1')
else:
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    for elem in fib:
        print(elem, sep=' ', end=' ')