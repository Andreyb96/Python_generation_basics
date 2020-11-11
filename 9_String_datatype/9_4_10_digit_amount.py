s = input()
counter = 0

for elem in s:
    if elem.isdigit():
        counter += 1

print(counter)