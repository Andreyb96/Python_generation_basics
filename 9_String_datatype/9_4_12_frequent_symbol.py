s = input()
counter = 0
freq = ''

for elem in s:
    if (s.count(elem) > counter):
        freq = elem
        counter = s.count(elem)
print(freq)