a, b = [int(input()) for i in range(2)]

for i in range(a, b+1):
    counter = 0
    for j in range(1, i):
        if i%j==0:
            counter += 1
    if counter == 1:
        print(i)