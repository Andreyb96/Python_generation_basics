from math import *
a, b, c = [float(input()) for _ in 'abc']

d = b**2-4*a*c

if d>0:
    print(min(((-1)*b - sqrt(d))/(2*a), ((-1)*b + sqrt(d))/(2*a)))
    print(max(((-1)*b - sqrt(d))/(2*a), ((-1)*b + sqrt(d))/(2*a)))
elif d==0:
    print((-1)*b/(2*a))
else:
    print('Нет корней')