l = [int(input()) for i in range(10)]

prod  = 1

for elem in l:
    if elem!=0:
        prod *= elem
print(prod)