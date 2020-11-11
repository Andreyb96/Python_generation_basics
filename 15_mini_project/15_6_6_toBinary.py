DICTIONARY = {
	10 : 'A',
	11 : 'B',
	12 : 'C',
	13 : 'D',
	14 : 'E',
	15 : 'F'
}


def toBinary(number, divider):
	result = ''
	while number >= divider:
		if int(number%divider) in DICTIONARY:
			result += DICTIONARY[int(number%divider)]
		else:
			result += str(int(number%divider))
		number /= divider
	if int(number) in DICTIONARY:
			result += DICTIONARY[int(number)]
	else:
		result += str(int(number))
	return result[::-1]


n = int(input())

print(toBinary(n, 2))
print(toBinary(n, 8))
print(toBinary(n, 16))