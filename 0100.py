limit = 10 ** 12

x1 = 1
y1 = 1
[x, y] = [x1, y1]

while True:
	[x, y] = [x * x1 + 2 * y * y1, x1 * y + y1 * x]
	# print(x, y)
	if (x + 1) % 2 != 0: continue
	if (y + 1) % 2 != 0: continue
	print((y + 1) // 2, (x + 1) // 2)
	if 2 * limit - 1 < x: break


# not really working