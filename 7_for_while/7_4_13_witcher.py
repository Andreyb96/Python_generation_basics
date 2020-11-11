n = int(input())
counter = 0

while n!=0:
    if n>=25:
        counter += n//25
        n %= 25
    elif n >= 10:
        counter += n//10
        n %= 10
    elif n >= 5:
        counter += n//5
        n %= 5
    else:
        counter += n
        n = 0

print(counter)