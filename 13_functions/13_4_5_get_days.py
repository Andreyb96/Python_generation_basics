def get_days(month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month==2:
        return 28
    else:
        return 31

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))