cities = [input() for i in 'abc']

l = [len(elem) for elem in cities]

print(cities[l.index(min(l))])
print(cities[l.index(max(l))])