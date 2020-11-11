def is_correct_bracket(text):
    openBrackets = 0
    for elem in text:
        if elem == '(':
            openBrackets += 1
        elif elem == ')':
            if openBrackets==0:
                return False
            else:
                openBrackets -= 1
    if openBrackets == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))