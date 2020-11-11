s = input()

if s.find('f')==-1:
    print(-2)
elif s.count('f')==1:
    print(-1)
else:
    new_str = s[:s.find('f')] + s[s.find('f')+1:]
    print(new_str.find('f') + 1)