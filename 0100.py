import math

r = math.sqrt(0.5)
i = 22
# i = 1000000000000
found = False


while not found:
	i += 1
	a = int(i * r)

	while True:
		n = a * (a - 1) * 2
		m = i * (i - 1)

		if n == m:
			found = True
			print(a, i)
			break
		elif n > m:
			break

		a += 1

# not really working