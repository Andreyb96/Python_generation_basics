l = [len(input()) for i in 'abc']

l.sort()

sor = set()

for i in range(1,len(l)):
    sor.add(l[i] - l[i-1])
    
if len(sor)==1:
    print('YES')
else:
    print('NO')