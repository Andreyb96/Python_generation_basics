def is_prime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    if num != 1:
        return True
    else:
        return False

def get_next_prime(num):
    flag = True
    cur = num + 1
    while flag:
        if is_prime(cur):
            flag = False
        else:
            cur += 1
    return cur

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))