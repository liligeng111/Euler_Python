# pell equation
# let lengh of edges be a, a, a+1(similar of a-1)
# s = sqrt((3a+1)(a-1)(a+1)(a+1))
# thus (3a+1)(a-1) = k^2 => (3a-1)^2 - 3k^2 = 4 => devide by 4

limit = 10 ** 9
# square = [0] * (limit//3)

x1 = 2
y1 = 1
[x, y] = [x1, y1]
s = 0

while True:
	[x, y] = [x * x1 + 3 * y * y1, x1 * y + y1 * x]
	if 2 * x + 2 > limit: break
	# print(x, y)
	if (2 * x + 1) % 3 != 0: continue
	# print(x*2+2)
	s += 2 * x + 2

# for a, a, a-1
x1 = 2
y1 = 1
[x, y] = [x1, y1]

while True:
	[x, y] = [x * x1 + 3 * y * y1, x1 * y + y1 * x]
	if 2 * x - 2 > limit: break
	if (2 * x - 1) % 3 != 0: continue
	# print(x, y)
	s += 2 * x - 2

print(s)

