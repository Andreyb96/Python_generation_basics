n = int(input())
sum = 0

while n > 9:
    while n/10!=0:
        sum += n%10
        n //= 10
    n = sum
    sum = 0
    
print(n)