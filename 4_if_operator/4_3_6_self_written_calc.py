a, b = [int(input()) for _ in 'ab']
operation = input()

if (operation == '+'):
    print(a+b)
elif (operation == '-'):
    print(a-b)
elif (operation == '*'):
    print(a*b)
elif (operation == '/' and b!=0):
    print(a/b)
elif (operation == '/' and b==0):
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')    