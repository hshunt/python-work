class Maps():
	
	def __init__(self, maps):
		self.map_data = []

		for line in maps:
			line = line.strip('\n')
			line = (line,)
			self.map_data.append(line)

	def show_map(self, x_inc, y_inc):
		x = 0
		y = 1

		for line in self.map_data:
			string = line[0]
			if y == y_inc:
				y = 0
				x+=x_inc
				if x >= len(string):
					x = x - len(string)
				print(f"{string[x]} in space {x+1}")
			print(f"{string}\n")
			y+=1

	def tree(self, x_inc, y_inc):
		x = 0
		cnt = 0
		self.trees = 0
		y = 1
		z = 0

		for line in self.map_data:
			string = line[0]
			if y == y_inc:
				y = 0
				if z > 0:
					x+=x_inc
				if x >= len(string):
					x = x - (len(string))
				if string[x] == "#":
					self.trees+=1
				cnt+=1
			z+=1
			y+=1

		print(f"\ntrees= {self.trees}")
		print(f"count= {cnt}")
		return self.trees

	def multiply(self, *args):
		result = 1
		for arg in args:
			result = result * arg
			print(result)

with open('f:\\Documents\\GitHub\\python-work\\Advent_of_code\\aoc_day3\\input.txt', 'r') as maps:
	tobo_map = Maps(maps)

	trees_0 = tobo_map.tree(1, 1)
	trees_1 = tobo_map.tree(3, 1)
	trees_2 = tobo_map.tree(5, 1)
	trees_3 = tobo_map.tree(7, 1)
	trees_4 = tobo_map.tree(1, 2)
	tobo_map.multiply(trees_0, trees_1, trees_2, trees_3, trees_4)

# with open('f:\\Documents\\GitHub\\python-work\\Advent_of_code\\aoc_day3\\test.txt', 'r') as test:
# 	tobo_map = Maps(test)

# 	trees_0 = tobo_map.tree(1, 1)
# 	trees_1 = tobo_map.tree(3, 1)
# 	trees_2 = tobo_map.tree(5, 1)
# 	trees_3 = tobo_map.tree(7, 1)
# 	trees_4 = tobo_map.tree(1, 2)

# 	# tobo_map.tree(1, 1)
	# tobo_map.tree(3, 1)
	# tobo_map.tree(5, 1)
	# tobo_map.tree(7, 1)
	# tobo_map.tree(1, 2)

	# tobo_map.show_map(1, 2)
	# tobo_map.multiply(trees_0, trees_1, trees_2, trees_3, trees_4)