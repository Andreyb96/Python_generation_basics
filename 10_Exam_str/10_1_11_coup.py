s = input()
last_idx = len(s) - s[::-1].find('h') - 1
first_idx = s.find('h')
print(s[:first_idx+1] + s[first_idx+1:last_idx][::-1] + s[last_idx:])