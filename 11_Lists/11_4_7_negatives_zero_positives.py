n = int(input())
l = [int(input()) for _ in range(n)]
output = []
for elem in l:
    if elem < 0:
        output.append(elem)
        
for elem in l:
    if elem == 0:
        output.append(elem)
        
for elem in l:
    if elem > 0:
        output.append(elem)

print(*output, sep='\n')