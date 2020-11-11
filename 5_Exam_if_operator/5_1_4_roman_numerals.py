rim = {1:'I', 2: 'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X'}

n = int(input())

if n not in rim:
    print('ошибка')
else:
    print(rim[n])