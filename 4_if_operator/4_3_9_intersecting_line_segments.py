a1, b1, a2, b2 = [int(input()) for _ in 'abcd']

if (a1 == b2):
    print(a1)
elif (b1==a2):
    print(b1)
elif (a2 <= a1 and  b2 > a1 and b2 <= b1):
    print('{0} {1}'.format(a1, b2))
elif (a2 <= a1 and  b2 > a1 and b2 > b1):
    print('{0} {1}'.format(a1, b1))
elif (a1 <= a2 and  b1 > a2 and b1 <= b2):
    print('{0} {1}'.format(a2, b1))
elif (a1 <= a2 and  b1 > a2 and b1 > b2):
    print('{0} {1}'.format(a2, b2))
else:
    print('пустое множество')