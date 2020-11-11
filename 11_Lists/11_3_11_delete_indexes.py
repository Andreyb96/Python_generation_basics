n = int(input())
l = [int(input()) for _ in range(n)]
output = []

for i in range(len(l)):
    if i%2==0:
        output.append(l[i])

print(output)