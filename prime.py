import util

primes = [2, 3]
d_sum = [0]

def init(n):
	i = primes[-1]
	while i < n:
		i += 2 
		for num in primes:
			if num * num > i:
				primes.append(i)
				break
			if i % num == 0:
				break


def decompose(n):
	init(n)
	fac = {}
	i = 0
	while n > 1:
		if n % primes[i] == 0:
			n = int(n / primes[i])
			if primes[i] in fac:
				fac[primes[i]] += 1
			else:
				fac[primes[i]] = 1
		elif primes[i] * primes[i] > n:
			fac[n] = 1
			break
		else:
			i += 1
	return fac

# for i in range(2, 100):
# 	decompose(i)
# print(decom[28])
# init(100)
# init(1000001)
# print(primes)
# print(decompose(480))
# print(decompose(960))