s = input()
l = s.split(' ')
counter = 0

for i in range(len(l)):
    for j in range(i, len(l)):
        if i!=j and l[i]==l[j]:
            counter += 1
print(counter)