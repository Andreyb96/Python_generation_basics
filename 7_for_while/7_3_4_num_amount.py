a, b = [int(input()) for _ in 'ab']
counter = 0

for i in range(a, b+1):
    if i**3%10==4 or i**3%10==9:
        counter+=1

print(counter)