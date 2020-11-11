m, p, n = [int(input()) for _ in 'abc']
amount = m

for i in range(n):
    
    print(str(i+1) + ' ' + str(amount))
    amount = amount*(1 + p/100)