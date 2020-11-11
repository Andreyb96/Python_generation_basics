n = int(input())
l = [input() for _ in range(n)]
search = input()
output = []

for i in l:
    if search.lower() in i.lower():
        output.append(i)
        
print(*output, sep = '\n')