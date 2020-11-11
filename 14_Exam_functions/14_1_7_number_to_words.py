def number_to_words(num):
    decades = { 10 : 'десять', 20 : 'двадцать', 30 : 'тридцать', 40 : 'сорок', 50 : 'пятьдесят', 60 : 'шестьдесят', 70 : 'семьдесят', 80 : 'восемьдесят', 90 : 'девяносто'}
    numbers = { 1 : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять', 6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять'}
    unusual = {11 : 'одиннадцать', 12 : 'двенадцать', 13 : 'тринадцать', 14 : 'четырнадцать', 15 : 'пятнадцать', 16 : 'шестнадцать', 17 : 'семнадцать', 18 : 'восемнадцать', 19 : 'девятнадцать'}
    if num in decades:
        return decades[num]
    elif num in numbers:
        return numbers[num]
    elif num in unusual:
        return unusual[num]
    else:
        first = num // 10 * 10
        second = num % 10
        return decades[first] + ' ' + numbers[second]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))