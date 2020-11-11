def print_digit_sum(num):
    sum = 0
    while num > 0:
        sum += num%10
        num //= 10
    print(sum)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)