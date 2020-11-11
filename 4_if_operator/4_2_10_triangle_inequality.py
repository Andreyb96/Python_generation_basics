a, b, c = [int(input()) for _ in 'abc']

if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')