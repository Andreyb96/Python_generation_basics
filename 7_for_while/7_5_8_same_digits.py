s = input()
l = set()

for elem in s:
    l.add(elem)

if len(l)==1:
    print('YES')
else:
    print('NO')