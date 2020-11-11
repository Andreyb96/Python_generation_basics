s = input()
s = s.lower()
vovels = 0
letters = 0
allVovels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
allLetters = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

for elem in s:
    if elem in allVovels:
        vovels += 1
    elif elem in allLetters:
        letters += 1

print('Количество гласных букв равно {0}'.format(vovels))
print('Количество согласных букв равно {0}'.format(letters))