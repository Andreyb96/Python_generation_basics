start = ord('a')
l = []

for i in range(26):
    l.append(chr(start+i)*(i+1))
    
print(l)