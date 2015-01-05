import math

r = math.sqrt(0.5)
# i = 200000000
i = 10 ** 6
found = False

def is_square(n):
	root = int(math.sqrt(n))
	return root * root == n

while not found:
	i += 1
	if is_square(2 * i * (i - 1) + 1):
		found = True
		print(i)

# not really working