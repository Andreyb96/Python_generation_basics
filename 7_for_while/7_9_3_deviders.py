a, b = [int(input()) for _ in range(2)]
max = 0

for i in range(a, b+1):
    counter = 0
    for j in range(1, i+1):
        if i%j==0:
            counter += j
    if counter > max:
        max = counter
        idx = i
print(idx, max)