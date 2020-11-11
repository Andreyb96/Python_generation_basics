n = int(input())
l = [input() for _ in range(n)]
k = int(input())
search = [input() for _ in range(k)]
output = []

for i in l:
    flag = True 
    for j in search:
        if j.lower() not in i.lower():
            flag = False
    if flag:
        output.append(i)
        
print(*output, sep = '\n')