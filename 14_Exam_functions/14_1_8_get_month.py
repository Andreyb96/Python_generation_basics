def get_month(language, number):
    monthsRu = { 1 : 'январь', 2 : 'февраль', 3 : 'март', 4 : 'апрель', 5 : 'май', 6 : 'июнь', 7 : 'июль', 8 : 'август', 9 : 'сентябрь', 10 : 'октябрь', 11 : 'ноябрь', 12 : 'декабрь'}
    monthsEn = { 1 : 'january', 2 : 'february', 3 : 'march', 4 : 'april', 5 : 'may', 6 : 'june', 7 : 'july', 8 : 'august', 9 : 'september', 10 : 'october', 11 : 'november', 12 : 'december'}
    if language == 'ru':
        return monthsRu[number]
    else:
        return monthsEn[number]
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))