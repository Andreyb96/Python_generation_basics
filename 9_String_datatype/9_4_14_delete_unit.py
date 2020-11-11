s = input()

print(s.replace(s[s.find('h'):len(s) - s[::-1].find('h')], ''))
