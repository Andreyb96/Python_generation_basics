def merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    l = list1
    return l

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))