n = int(input())

sum = 0

for i in range(1, n+1):
    if i**2%10==2 or i**2%10==5 or i**2%10==8:
        sum += i
    
print(sum)