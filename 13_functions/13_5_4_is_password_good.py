def is_password_good(password):
    flag1 = False
    flag2 = False
    flag3 = False
    for elem in password:
        if elem.isupper():
            flag1 = True
        if elem.islower():
            flag2 = True
        if elem.isdigit():
            flag3 = True
    if len(password) >= 8 and flag1 and flag2 and flag3:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))