languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

new = []

for i in range(len(languages)-1, -1, -1):
    new.append(languages[i])
print(new)