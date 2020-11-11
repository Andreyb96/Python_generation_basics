from math import sqrt

def solve(a, b, c):
    d = b**2 - 4*a*c
    first = (-1 * b - sqrt(d))/(2*a)
    second = (-1 * b + sqrt(d))/(2*a)
    return min(first, second), max(first, second)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)