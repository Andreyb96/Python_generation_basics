x1, y1, x2, y2 = [int(input()) for _ in 'abcd']

if abs(x1-x2)<=1 and abs(y1-y2)<=1:
    print('YES')
else:
    print('NO')