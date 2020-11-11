s = input()
flag = True
for i in range(len(s)):
    if s[i]!=s[(-1)*i-1]:
        flag = False

if flag:
    print('YES')
else:
    print('NO')