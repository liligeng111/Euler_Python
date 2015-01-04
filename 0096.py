from suduko import Suduko

f = open("0096.txt", 'r')
s = 0

for line in f:
	if line.find("Grid") != -1:
		S = Suduko()
		num = line[:7] + " :"
		y = 0
	else:
		for x in range(0, 9):
			S.set(x, y, int(line[x]))
		y += 1
		if y == 9:
			if not S.solve(): break
			n = 100 * S.get(0, 0) + 10 * S.get(1, 0) + S.get(2, 0)
			s += n
			print(num, s, n)
	# print(line)
