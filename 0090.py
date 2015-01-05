import itertools

digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

tup = itertools.combinations(digit, 6)
com = []

for t in tup:
	c = list(t)
	if 6 in c and 9 not in c: c.append(9)
	if 9 in c and 6 not in c: c.append(6)
	c.sort()
	com.append(c)

def can_display(a, b, la, lb):
	if a in la and b in lb: return True
	if b in la and a in lb: return True
	return False

def can_display_square(la, lb):
	if not can_display(0, 1, la, lb): return False
	if not can_display(0, 4, la, lb): return False
	if not can_display(0, 9, la, lb): return False
	if not can_display(1, 6, la, lb): return False
	if not can_display(2, 5, la, lb): return False
	if not can_display(3, 6, la, lb): return False
	if not can_display(4, 9, la, lb): return False
	if not can_display(6, 4, la, lb): return False
	if not can_display(8, 1, la, lb): return False
	return True

count = 0
for i in range(len(com)):
	for j in range(i):
		if can_display_square(com[i], com[j]):
			# print(com[i], com[j])
			count += 1
print(count)