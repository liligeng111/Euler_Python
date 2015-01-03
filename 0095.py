import math
import prime
import util

def divisor_sum(n):
	fac = prime.decompose(n)

	S = 1
	for key in fac:
		num = fac[key] + 1
		S *= (key ** num - 1) / (key - 1)
		# print(S)
	return int(S - n)

def length(n):
	li = []
	i = 0
	r = -1
	while n <= 1000000:
		try:
			i = li.index(n)
			r = len(li)
			break;
		except ValueError:
			pass # no match

		# print(n)
		if (L[n] != 0):
			r = -2
			break

		li.append(n)
		n = S[n]

	# print(li)
	for j in range(0, len(li)):
		L[li[j]] = r - i if j >= i else -2
		# print(j, i, L[li[j]])


S = [0] * 1000001
L = [0] * 1000001

prime.init(1000001)
# print(divisor_sum(2))
# print(divisor_sum(4))
# print(divisor_sum(7))
# print(divisor_sum(14))
# print(divisor_sum(28))
# print(divisor_sum(12496))

for i in range(0, 1000000):
	S[i] = int(divisor_sum(i))

# print(S[12496])

# print(length(9464))
M = 0

for i in range(0, 1000000):
	 if L[i] == 0: length(i)
	 if L[i] > M:
	 	M = L[i]
	 	print(i, M)

# print(L[12496])
# print(prime.primes)

