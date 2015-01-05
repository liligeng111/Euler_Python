

limit = 50 + 1
count = 0

def is_right(x1, y1, x2, y2):
	#right angle at origin
	if x1 == 0 and y2 == 0:
		return True

	#righe angle at x1, y1
	if y1 * (y2 - y1) + x1 * (x2 - x1) == 0:
		# print(x1, y1, x2, y2)
		return True

	#righe angle at x2, y2
	if y2 * (y1 - y2) + x2 * (x1 - x2) == 0:
		return True

	return False

for x1 in range(limit):
	for y1 in range(limit):
		for x2 in range(limit):
			for y2 in range(limit):
				#origin point
				if [x1, y1] == [0, 0] or [x2, y2] == [0, 0]:
					continue

				#count once
				if (y2 * x1) >= (y1 * x2):
					continue

				if is_right(x1, y1, x2, y2):
					count += 1

print(count)


