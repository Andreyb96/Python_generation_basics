from numpy import prod

s = input()
l = [int(i) for i in s]

print(sum(l))
print(len(l))
print(prod(l))
print(sum(l)/len(l))
print(l[0])
print(l[0] + l[-1])