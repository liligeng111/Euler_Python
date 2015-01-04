import itertools
import copy

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

	def remove_choice(self, x, y, list):
		for n in list:
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
			#Truns out it is faster not to deduct......FUCK
			# self.check_subset()
			if self.solved == 81:
				return self.check_correct()

		#cannot deduct, begin trying
		return self.trial()

	def trial(self):
		[x, y] = self.most_likely()
		if [x, y] == [-1, -1]: return False
		pool = self.choice[x][y]
		for i in pool:
			foo = copy.deepcopy(self)
			foo.set(x, y, i)
			if foo.solve():
				self.set(x, y, i)
				return self.solve()
		# print("Cannot solve this puzzle")
		# self.show()
		return False

	def most_likely(self):
		for i in range(2, 9):
			for x in range(0, 9):
				for y in range(0, 9):
					if len(self.choice[x][y]): return [x, y]
		#wrong try, no choices left
		return [-1, -1]

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
			remain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
			for coord in g:
				if self.board[coord[0]][coord[1]] != 0:
					remain.remove(self.board[coord[0]][coord[1]])

			com = []
			for i in range(1, len(remain)): com += list(itertools.combinations(remain, i))
			for c in com:
				c = list(c)
				pointing = []
				subset = []
				for coord in g:
					if self.board[coord[0]][coord[1]] != 0: continue
					for i in c:
						if i in self.choice[coord[0]][coord[1]]:pointing.append(coord)

					is_subset = True
					for i in self.choice[coord[0]][coord[1]]:
						if i not in c:
							is_subset = False
							break
					if is_subset:
						subset.append(coord)

				#subset found!
				if len(subset) == len(c):
					# self.show()
					# print(subset, c)
					for coord in g:
						if coord not in subset: self.remove_choice(coord[0], coord[1], c)
					# self.show()
					break


				# leave for only_choice
				if len(pointing) == 1: continue
				#not pointing
				if len(pointing) == 0: continue

				for tg in Suduko.group:
					is_pointint = True
					for sc in pointing:
						if sc not in tg:
							is_pointint = False
							break

					if not is_pointint: continue
					for coord in tg:
						if coord in pointing: continue
						# print(c, tg, pointing)
						# self.show()
						self.remove_choice(coord[0], coord[1], c)
					# self.show()
					# raise system.exit

