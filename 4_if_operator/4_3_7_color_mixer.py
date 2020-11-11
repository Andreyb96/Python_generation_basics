color1, color2 = [input() for _ in 'ab']
colors = ['красный', 'синий', 'желтый']

if color1 not in colors or color2 not in colors:
    print('ошибка цвета')
elif {color1, color2} == {'красный', 'синий'}:
    print('фиолетовый')
elif {color1, color2} == {'красный', 'желтый'}:
    print('оранжевый')
elif {color1, color2} == {'синий', 'желтый'}:
    print('зеленый')