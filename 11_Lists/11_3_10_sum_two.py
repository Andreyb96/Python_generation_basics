n = int(input())
l = [int(input()) for _ in range(n)]
output = []

for i in range(len(l)-1):
    output.append(l[i] + l[i+1])

print(output)