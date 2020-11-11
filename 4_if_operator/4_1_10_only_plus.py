l = [int(input()) for _ in 'abc']
l2 = []

for elem in l:
    if elem > 0:
        l2.append(elem)
        
print(sum(l2))