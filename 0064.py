import math
import util

def period(n):
	a = int(math.sqrt(n))
	root = math.sqrt(n)
	l_a = [a]
	b = 1
	l_b = [b]

	# square number
	if root == a: return 0

	#a + (b*sqrt(n) + x)/y
	x = -a
	l_x = [x]
	y = 1
	l_y = [y]
	i = 0
	while True:
		# print(a, b, x, y)
		i += 1
		a = int(y / (b * root + x))
		y = l_b[-1] * l_b[-1] * n - l_x[-1] * l_x[-1]
		b = l_b[-1] * l_y[-1]
		x = - a * y - l_x[-1] * l_y[-1]

		g = util.gcd(y, b)
		g = util.gcd(g, x)
		y = y // g
		x = x // g
		b = b // g
		l_a.append(a)
		l_b.append(b)
		l_x.append(x)
		l_y.append(y)

		for i in range(len(l_a) - 1):
			if a == l_a[i] and b == l_b[i] and x == l_x[i] and y == l_y[i]:
				# print(len(l_a), i)
				return len(l_a) - i - 1

count = 0
for i in range(2, 10001):
	if period(i) % 2 == 1: count += 1
print(count)