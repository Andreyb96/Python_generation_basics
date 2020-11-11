s = input()

l = [int(i) for i in s]
flag = True

for i in range(len(l)-1):
    if l[i] < l[i+1]:
        flag = False

if flag:
    print('YES')
else:
    print('NO')