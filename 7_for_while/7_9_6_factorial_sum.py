def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum


n = int(input())
l = [factorial(i) for i in range(1, n+1)]
print(sum(l))