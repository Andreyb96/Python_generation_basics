n = int(input())
strings = [input() for i in range(n)]
counter = 0

for s in strings:
    if s.count('11')>2:
        counter += 1
        
print(counter)