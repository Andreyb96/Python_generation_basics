a, b, c = [int(input()) for _ in 'abc']

if a!=b and b!=c and a!=c:
    print('Разносторонний')
elif a==b==c:
    print('Равносторонний')
else:
    print('Равнобедренный')