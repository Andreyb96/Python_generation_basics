s = input()
new_str = ''
for i in range(len(s)):
    if i%3!=0:
        new_str += s[i]
print(new_str)
