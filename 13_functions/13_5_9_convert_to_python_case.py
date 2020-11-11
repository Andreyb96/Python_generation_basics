def convert_to_python_case(text):
    s = ''
    for elem in text:
        if elem.isupper():
            if s == '':
                s += elem.lower()
            else:
                s += '_' + elem.lower()
        else:
            s += elem
    return s

text = input()

print(convert_to_python_case(text))