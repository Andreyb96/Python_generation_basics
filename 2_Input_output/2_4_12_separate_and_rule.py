n = int(input())
s = str(n)
for i in range(4):
    s += '-'*3 + str((i+2)*n)
    
print(s)