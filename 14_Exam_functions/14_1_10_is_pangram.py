def is_pangram(text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in text.lower():
        if letter in letters:
            letters.remove(letter)
    return len(letters) == 0

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))