class Suduko:

	group = []
	for i in range(0, 9):
		h = []
		v = []
		g = []
		for j in range(0, 9): h.append([i, j])
		for j in range(0, 9): v.append([j, i])
		for j in range(0, 9): g.append([3*(i//3) + j//3, 3*(i%3) + j%3])
		group.append(h)
		group.append(v)
		group.append(g)

	def __init__(self):
		self.board = []
		self.choice = []
		self.changed = True
		self.init = True
		self.solved = 0
		for y in range(0, 9):
			self.board.append([0]*9)
			c = []
			for x in range(0, 9):
				c.append([1,2,3,4,5,6,7,8,9])
			self.choice.append(c)

	def set(self, x, y, n):
		self.board[x][y] = n
		if n == 0: return
		self.solved += 1
		self.changed = True
		self.choice[x][y] = []
		# if not self.init: print("set: ", x, y, n)
		for g in Suduko.group:
			if [x, y] not in g: continue
			# print(x, y, n)
			# self.show_choice(8, 0)
			for coord in g:
				if n in self.choice[coord[0]][coord[1]]: self.choice[coord[0]][coord[1]].remove(n)

	def remove_choice(self, x, y, n):
		if n in self.choice[x][y]:
			self.choice[x][y].remove(n)
			self.changed = True

	def show(self):
		# for y in range(0, 9):
		# 	print("", end="|")
		# 	for x in range(0, 9):
		# 		print(self.board[x][y], end="|")
		# 	print("")
		# print("----------------------")
		# print(self.board)
		print("-------------------------------------------------------")
		for y in range(0, 27):
			for x in range(0, 27):
				if x % 3 == 0: print("", end="|")
				if self.board[x//3][y//3] != 0:
					print(self.board[x//3][y//3], end="")
				else:
					can = 3 * (y % 3) + x % 3 + 1
					if can in self.choice[x//3][y//3]:
						print(can, end="")
					else:
						print(" ", end="")
				if x % 3 == 0: print("", end=" ")
				if x % 3 == 1: print("", end=" ")
			print("|")
			if y % 3 == 2: print("-------------------------------------------------------")
		# print(self.board)

	def get(self, x, y):
		return self.board[x][y]

	def show_choice(self, x, y):
		print(self.choice[x][y])

	def check_correct(self):
		for g in Suduko.group:
			s = 0
			for coord in g: s += self.board[coord[0]][coord[1]]
			if s != 45: 
				print("Solve result incorrect")
				self.show()
				return False
		return True

	def solve(self):
		self.init = False
		# self.only_choice()
		while self.changed:
			self.changed = False
			self.only_choice()
			self.check_subset()
			if self.solved == 81:
				return self.check_correct()
		print("Cannot solve this puzzle")
		self.show()
		return False

	def only_choice(self):
		for x in range(0, 9):
			for y in range(0, 9):
				if len(self.choice[x][y]) == 1:
					self.set(x, y, self.choice[x][y][0])

		for g in Suduko.group:
			for i in range(1, 10):
				found = []
				exist = False
				for coord in g:
					if self.board[coord[0]][coord[1]] == i:
						exist = True
						break
					if i in self.choice[coord[0]][coord[1]]: found.append(coord)
				if not exist and len(found) == 1:
					self.set(found[0][0], found[0][1], i)

	def check_subset(self):		
		for g in Suduko.group:
			count = 0
			for coord in g:
				if self.board[coord[0]][coord[1]] != 0:
					count += 1

			for i in range(1, 10):
				found = []
				for coord in g:
					if i in self.choice[coord[0]][coord[1]]: found.append(coord)

				#found all
				if len(found) == 9 - count: continue
				# leave for only_choice
				if len(found) == 1: continue
				#not found
				if len(found) == 0: continue

				for tg in Suduko.group:
					subset = True
					for sc in found:
						if sc not in tg:
							subset = False
							break

					if not subset: continue
					for coord in tg:
						if coord in found: continue
						self.remove_choice(coord[0], coord[1], i)