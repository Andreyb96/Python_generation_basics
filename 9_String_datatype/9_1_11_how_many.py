s = input()
plusCounter = 0
starCounter = 0

for elem in s:
    if elem=='+':
        plusCounter += 1
    elif elem=='*':
        starCounter += 1

print('Символ + встречается {0} раз'.format(plusCounter))
print('Символ * встречается {0} раз'.format(starCounter))