s = input()
counter = 0

for elem in s:
    if elem.islower():
        counter += 1
        
print(counter)