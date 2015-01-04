import math

f = open("0099.txt", 'r')
m = 0
i = 1

for line in f:
	pair = line.split(',')
	power = math.log(int(pair[0])) * int(pair[1])
	if power >= m:
		m = power
		print(i)
	i += 1