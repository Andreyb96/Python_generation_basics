def number_of_factors(num):
    l = []
    for i in range(1, num+1):
        if num%i==0:
            l.append(i)
    return len(l)

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))