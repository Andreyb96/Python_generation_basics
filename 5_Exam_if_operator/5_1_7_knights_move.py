x1, y1, x2, y2 = [int(input()) for i in 'abcd']

if (abs(x1-x2) == 1 and abs(y1-y2) == 2) or (abs(x1-x2) == 2 and abs(y1-y2) == 1):
    print('YES')
else:
    print('NO')