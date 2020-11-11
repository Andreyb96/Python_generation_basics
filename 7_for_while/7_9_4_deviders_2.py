n = int(input())

for i in range(1, n+1):
    counter = 0
    for j in range(1, i+1):
        if i%j==0:
            counter += 1
    print(str(i) + '+'*counter)