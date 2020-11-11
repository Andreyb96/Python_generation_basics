n = int(input())

digit1 = n//1000;
digit2 = n//100%10;
digit3 = n//10%10;
digit4 = n%10

print('Цифра в позиции тысяч равна {0}'.format(digit1))
print('Цифра в позиции сотен равна {0}'.format(digit2))
print('Цифра в позиции десятков равна {0}'.format(digit3))
print('Цифра в позиции единиц равна {0}'.format(digit4))