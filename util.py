def unique_sum(n):
	s = 0
	n.sort()
	index = n[0] - 1
	for num in n:
		if num > index:
			s += num
			index = num

	return int(s)


def gcd(a, b):
	#a > b 
	if a < b: return gcd(b, a)
	if a % b == 0: return b
	return gcd(a % b, b)