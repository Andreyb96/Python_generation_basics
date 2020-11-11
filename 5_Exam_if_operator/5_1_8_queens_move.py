x1, y1, x2, y2 = [int(input()) for i in 'abcd']

if (x1==x2 or y1==y2) or (abs(x1-x2) == abs(y1-y2)):
    print('YES')
else:
    print('NO')