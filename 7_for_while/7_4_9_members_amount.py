s = input()
counter = 0
while (s not in ['стоп', 'хватит', 'достаточно']):
    counter += 1
    s = input()

print(counter)