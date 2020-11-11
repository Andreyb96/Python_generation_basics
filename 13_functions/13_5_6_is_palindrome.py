def is_palindrome(text):
    s = ''
    for elem in text:
        if elem.isalpha():
            s += elem.lower()
    for i in range(len(s)//2):
        for j in range(len(s)//2):
            if s[i] != s[::-1][j] and i==j:
                return False
    return True

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))