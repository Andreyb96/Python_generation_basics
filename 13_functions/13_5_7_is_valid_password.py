def is_valid_password(password):
    a , b, c = password.split(':')
    isSimple = True
    for i in range(2, int(b)):
        if int(b)%i==0:
            isSimple = False
    if a == a[::-1] and int(c)%2 == 0 and isSimple:
        return True
    else:
        return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))