import math

def next(n):
	s = 1
	i = 2

	while i * i < n:
		if n % i == 0:
			s += i + int(n/i)
		i += 1

	return s

def length(n):
	li = []
	r = -1
	while n <= 1000000:
		if (L[n] != 0):
			if L[n] == -1:
				r = -1
			else:
				r = len(li) + L[n]
			break

		li.append(n)
		n = next(n)
		try:
			i = li.index(n)
			r = len(li)
			break;
		except ValueError:
			i = -1 # no match

	for e in li:
		# print(e, r)
		L[e] = r
	return r;

M = 0
i = 1
B = 10 * 10000
L = [0] * 1000001

# print(length(12496))

while i < B:
	i += 1
	if L[i] != 0:
		continue

	l = length(i)
	if (l > M):
		M = l
		print (i, l)
