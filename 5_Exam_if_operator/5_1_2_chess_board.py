x1, y1, x2, y2 = [int(input()) for i in 'abcd']

if ((x1+y1)%2==0 and (x2+y2)%2==0) or ((x1+y1)%2==1 and (x2+y2)%2==1):
    print('YES')
else:
    print('NO')