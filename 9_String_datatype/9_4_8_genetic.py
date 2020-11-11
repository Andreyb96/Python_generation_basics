s = input()
s = s.lower()
a = 0
g = 0
c = 0
t = 0

for elem in s:
    if elem == 'а':
        a += 1
    elif elem == 'г':
        g += 1
    elif elem == 'ц':
        c += 1
    else:
        t += 1

print('Аденин: ' + str(a))
print('Гуанин: ' + str(g))
print('Цитозин: ' + str(c))
print('Тимин: ' + str(t))