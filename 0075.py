import util

def triple(m, n):
	if util.gcd(m, n) != 1: return []
	m2 = m * m
	n2 = n * n
	r = [m2 - n2, 2 * m * n, m2 + n2]
	r.sort()

	return r

limit = 1500000
unique = []

for m in range(1, limit):
	mm = 2 * m * m
	if (mm > limit): break
	start = m % 2 + 1
	for n in range(start, m, 2):
		length = mm + 2 * m * n
		if (length > limit): break
		# l = triple(m, n)
		# print(l)
		if util.gcd(m, n) != 1: continue
		unique.append(length)

test = [0] * (limit // 2 + 1)
for l in unique:
	h = l // 2
	for i in range(h, limit // 2 + 1, h):
		test[i] += 1

count = 0
for i in range(len(test)):
	# print(2 * i, test[i])
	if test[i] == 1:
		count += 1

print(count)