s = input()

if s.find('f')==-1:
    print('NO')
elif s.count('f')==1:
    print(s.find('f'))
else:
    print(str(s.find('f')) + ' ' + str(len(s) - s[::-1].find('f') - 1))