from numpy import prod

n = input()
print(len([i for i in n if i=='3']))
lastDigit = n[-1]
print(len([i for i in n if i==lastDigit]))
print(len([i for i in n if int(i)%2==0]))
print(sum([int(i) for i in n if int(i) > 5]))
print(int(prod([int(i) for i in n if int(i) > 7])))
print(len([i for i in n if i=='0' or i=='5']))