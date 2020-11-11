s = input()
counter = 0

l = s.split(' ')

counter += l.count('a')
counter += l.count('an')
counter += l.count('the')

print('Общее количество артиклей: ' + str(counter))