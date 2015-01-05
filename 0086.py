import math

def M(n):
	count = 0
	# a > b > c
	for a in range(1, n + 1):
		for b in range(1, a + 1):
			for c in range(1, b + 1):
				if is_integer(a, b, c): count += 1
	return count

def is_integer(a, b, c):
	return False
	l_a = a * a + (b + c) * (b + c)
	l_b = b * b + (a + c) * (a + c)
	l_c = c * c + (a + b) * (a + b)
	s = l_a if l_a < l_b else l_b
	s = s if s < l_c else l_c
	root = math.sqrt(s)
	return root == int(root)

# i = 1
# while i < 200:
# 	i += 1
# 	if M(i) > 5000000:
# 		print(i, M(i))
# 		break 

print(M(1000))