s = input()
counter = 0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        counter += 1
print(counter)