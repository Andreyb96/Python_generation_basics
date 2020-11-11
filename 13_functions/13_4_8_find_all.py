def find_all(target, symbol):
    l = []
    for i in range(len(target)):
        if target[i] == symbol:
            l.append(i)
    return l

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))