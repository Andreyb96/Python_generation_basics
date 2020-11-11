s = input()

isDigit = False

for elem in s:
    if elem.isdigit():
        isDigit = True
        
if isDigit:
    print('Цифра')
else:
    print('Цифр нет')