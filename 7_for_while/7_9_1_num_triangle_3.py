n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i

l = [i for i in range(1, sum+1)]    
counter = 0

for i in range(1, n+1):
    s = []
    for j in range(i):
        s.append(l[counter + j])
    counter += i
    print(*s)