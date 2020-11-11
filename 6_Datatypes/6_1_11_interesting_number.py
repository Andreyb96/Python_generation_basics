from statistics import median

n = int(input())

digit1 = n//100;
digit2 = n//10%10;
digit3 = n%10;

if max(digit1, digit2, digit3) - min(digit1, digit2, digit3) == median([digit1, digit2, digit3]):
    print('Число интересное')
else:
    print('Число неинтересное')