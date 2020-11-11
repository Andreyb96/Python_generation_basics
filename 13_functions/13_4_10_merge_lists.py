if __name__ == "__main__":
	n = int(input())
	l = []
	for i in range(n):
		l.extend(input().split())
	l2  = [int(i) for i in l]
	l2.sort()
	print(*l2)