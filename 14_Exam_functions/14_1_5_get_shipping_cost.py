def get_shipping_cost(quantity):
    return 1000 + 120 * (quantity - 1)

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))