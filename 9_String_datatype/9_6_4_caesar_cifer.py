n = int(input())
s = input()
encode = ''

for elem in s:
    if ord(elem) - ord('a') < n:
        encode += chr(ord(elem) - n + 26)
    else:
        encode += chr(ord(elem)-n)
print(encode)