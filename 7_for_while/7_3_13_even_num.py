l = [int(input()) for _ in range(10)]

flag = True

for elem in l:
    if elem%2==1:
        flag = False

if flag:
    print('YES')
else:
    print('NO')