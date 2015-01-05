
def possible_resultd(x1, x2, x3, x4):
	result = []
	permutation = []
	permutation.append([x1, x2, x3, x4])
	permutation.append([x1, x2, x4, x3])
	permutation.append([x1, x3, x2, x4])
	permutation.append([x1, x3, x4, x2])
	permutation.append([x1, x4, x2, x3])
	permutation.append([x1, x4, x3, x2])

	permutation.append([x2, x1, x3, x4])
	permutation.append([x2, x1, x4, x3])
	permutation.append([x2, x3, x1, x4])
	permutation.append([x2, x3, x4, x1])
	permutation.append([x2, x4, x1, x3])
	permutation.append([x2, x4, x3, x1])

	permutation.append([x3, x1, x2, x4])
	permutation.append([x3, x1, x4, x2])
	permutation.append([x3, x2, x1, x4])
	permutation.append([x3, x2, x4, x1])
	permutation.append([x3, x4, x1, x2])
	permutation.append([x3, x4, x2, x1])

	permutation.append([x4, x1, x3, x2])
	permutation.append([x4, x1, x2, x3])
	permutation.append([x4, x3, x1, x2])
	permutation.append([x4, x3, x2, x1])
	permutation.append([x4, x2, x1, x3])
	permutation.append([x4, x2, x3, x1])

	for [a, b, c, d] in permutation:
		result.append(a + b + c + d)
		result.append(a + b + c - d)
		result.append(a + b - c - d)
		result.append(a - b - c - d)

		result.append(a * b + c + d)
		result.append(a * b - c - d)
		result.append(a * b + c - d)	
		result.append(a / b + c + d)
		result.append(a / b - c - d)
		result.append(a / b + c - d)	

		result.append(a * b * c + d)
		result.append(a * b * c - d)
		result.append(a * b / c + d)	
		result.append(a * b / c - d)
		result.append(a / b / c + d)
		result.append(a / b / c - d)	

		result.append((a + b) * c + d)
		result.append((a + b) * c - d)
		result.append((a + b) / c + d)
		result.append((a + b) / c - d)
		result.append((a - b) * c + d)
		result.append((a - b) * c - d)
		result.append((a - b) / c + d)
		result.append((a - b) / c - d)

		result.append(a * b + c * d)
		result.append(a * b - c * d)
		result.append(a / b + c / d)	
		result.append(a / b - c / d)
		result.append(a * b + c / d)
		result.append(a * b - c / d)	
		result.append(a / b + c * d)
		result.append(a / b - c * d)

		result.append(a * b * c * d)
		result.append(a * b * c / d)
		result.append(a * b / c / d)
		result.append(a / b / c / d)

		result.append((a + b) * c * d)
		result.append((a + b) * c / d)
		result.append((a + b) / c / d)
		result.append((a - b) * c * d)
		result.append((a - b) * c / d)
		result.append((a - b) / c / d)

		#missing a / (b - c - d)...but it worked
		result.append((a + b + c) * d)
		result.append((a + b + c) / d)
		result.append((a + b - c) * d)
		result.append((a + b - c) / d)
		result.append((a - b - c) * d)
		result.append((a - b - c) / d)

		result.append(((a * b) + c) * d)
		result.append(((a * b) + c) / d)
		result.append(((a * b) - c) * d)
		result.append(((a * b) - c) / d)
		result.append(((a / b) + c) * d)
		result.append(((a / b) + c) / d)
		result.append(((a / b) - c) * d)
		result.append(((a / b) - c) / d)

		result.append((a + b) * (c + d))
		result.append((a + b) / (c + d))
		result.append((a + b) * (c - d))
		result.append((a + b) / (c - d))
		result.append((a - b) * (c - d))
		result.append((a - b) / (c - d))
		result.append((a - b) * (c + d))
		result.append((a - b) / (c + d))

	valid = []
	for i in result:
		if i <= 0: continue
		if i != int(i): continue
		if i not in valid: valid.append(int(i))

	valid.sort()
	return valid

def length(li):
	for i in range(len(li)):
		if li[i] != i + 1: return i

m = 0
for x1 in range(1, 10):
	for x2 in range(x1 + 1, 10):
		for x3 in range(x2 + 1, 10):
			for x4 in range(x3 + 1, 10):
				r = possible_resultd(x1, x2, x3, x4)
				l = length(r)
				if l > m:
					m = l
					print(x1, x2, x3, x4, " : ", l)