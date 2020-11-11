m,n = [int(input()) for _ in 'ab']

for i in range(m, n+1):
    if i%17==0 or i%10==9 or (i%3==0 and i%5==0):
        print(i)