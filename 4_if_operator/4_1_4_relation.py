n = int(input())

digit1 = n//1000;
digit2 = n//100%10;
digit3 = n//10%10;
digit4 = n%10

if digit1 + digit4 == digit2 - digit3:
    print('ДА')
else:
    print('НЕТ')