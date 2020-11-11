n = int(input())

if ((n>0 and n<11 or n>18 and n<29) and n%2==1) or ((n>10 and n<19 or n>28 and n<37) and n%2==0):
    print('красный')
elif ((n>0 and n<11 or n>18 and n<29) and n%2==0) or ((n>10 and n<19 or n>28 and n<37) and n%2==1):
    print('черный')
elif n==0:
    print('зеленый')
else:
    print('ошибка ввода')