x1, y1, x2, y2 = [int(input()) for i in 'abcd']

if abs(x1-x2) == abs(y1-y2):
    print('YES')
else:
    print('NO')