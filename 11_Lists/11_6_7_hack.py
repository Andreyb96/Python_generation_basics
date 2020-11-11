s = int(input().split('#')[1])

strings = [input() for i in range(s)]

for i in strings:
    i = i.split('#')[0].rstrip()
    print(i)