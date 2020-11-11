a, b, c = [int(input()) for _ in 'abc']

if b - a == c - b:
    print('YES')
else:
    print('NO')