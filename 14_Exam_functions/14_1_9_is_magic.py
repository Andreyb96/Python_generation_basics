def is_magic(date):
    day, month, year = date.split('.')
    return int(day) * int(month) == int(year) % 100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))