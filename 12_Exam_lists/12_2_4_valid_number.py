s = input()
template = '0123456789'

if (s[0]=='7' and s[1]=='-' and s[5]=='-' and s[9]=='-'):
    s = s[2:5] + s[6:9] + s[10:]
    if len([i for i in s if i in template]) == len(s):
        print('YES')
    else:
        print('NO')
elif (s[3]=='-' and s[7]=='-'):
    s = s[:3] + s[4:7] + s[8:]
    if len([i for i in s if i in template]) == len(s):
        print('YES')
    else:
        print('NO')
else:
    print('NO')