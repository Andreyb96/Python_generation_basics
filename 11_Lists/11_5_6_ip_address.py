l = input().split('.')
flag = True

for elem in l:
    if int(elem)>255:
        flag = False
if flag:
    print('ДА')
else:
    print('НЕТ')