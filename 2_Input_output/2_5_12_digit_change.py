n = int(input())

digit1 = n//100;
digit2 = n//10%10;
digit3 = n%10;

print(n)
print(digit1 * 100 + digit3 * 10 + digit2)
print(digit2 * 100 + digit1 * 10 + digit3)
print(digit2 * 100 + digit3 * 10 + digit1)
print(digit3 * 100 + digit1 * 10 + digit2)
print(digit3 * 100 + digit2 * 10 + digit1)