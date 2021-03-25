class Maps():
	
	def __init__(self, maps):
		self.map_data = []

		for line in maps:
			line = line.strip('\n')
			line = (line,)
			self.map_data.append(line)

	def show_map(self):
		x=-1

		for line in self.map_data:
			string = line[0]
			if x >= len(string):
				x = x - len(string) 
			print(string[x])
			print(f"{string}\n")
			x+=3

	def tree_0(self):
		x = 0
		cnt = 0
		self.trees = 0
		for line in self.map_data:
			string = line[0]
			if string[x] == "#":
				self.trees+=1
			x+=1
			cnt+=1
			if x >= len(string):
				x = x - len(string) 
		print(f"\ntrees= {self.trees}")
		print(f"count= {cnt}")

	def tree_1(self):
		x = 0
		cnt = 0
		self.trees_1 = 0
		for line in self.map_data:
			string = line[0]
			if string[x] == "#":
				self.trees_1+=1
			x+=3
			cnt+=1
			if x >= len(string):
				x = x - len(string) 
		print(f"\ntrees= {self.trees_1}")
		print(f"count= {cnt}")

	def tree_2(self):
		x = 0
		cnt = 0
		self.trees_2 = 0
		for line in self.map_data:
			string = line[0]
			if string[x] == "#":
				self.trees_2+=1
			x+=5
			cnt+=1
			if x >= len(string):
				x = x - len(string) 
		print(f"\ntrees= {self.trees_2}")
		print(f"count= {cnt}")

	def tree_3(self):
		x = 0
		cnt = 0
		self.trees_3 = 0
		for line in self.map_data:
			string = line[0]
			if string[x] == "#":
				self.trees_3+=1
			x+=7
			cnt+=1
			if x >= len(string):
				x = x - len(string) 
		print(f"\ntrees= {self.trees_3}")
		print(f"count= {cnt}")

	def tree_4(self):
		x = 0
		cnt = 0
		self.trees_4 = 0
		z = 0

		for line in self.map_data:
			string = line[0]
			if z == 2:
				z = 0
				x+=1
				if x >= len(string):
					x = x - len(string)
				elif string[x] == "#":
					self.trees_4+=1
				cnt+=1
			z+=1

		print(f"\ntrees= {self.trees_4}")
		print(f"count= {cnt}")

	def multiply(self):
		result = self.trees * self.trees_1 * self.trees_2 * self.trees_3 * self.trees_4

		print(result)


with open('f:\\Documents\\GitHub\\python-work\\Advent_of_code\\aoc_day3\\input.txt', 'r') as maps:
	tobo_map = Maps(maps)

	tobo_map.tree_0()
	tobo_map.tree_1()
	tobo_map.tree_2()
	tobo_map.tree_3()
	tobo_map.tree_4()

	tobo_map.multiply()
# with open('f:\\Documents\\GitHub\\python-work\\Advent_of_code\\aoc_day3\\test.txt', 'r') as test:
# 	tobo_map = Maps(test)

# 	tobo_map.tree_0()
# 	tobo_map.tree_1()
# 	tobo_map.tree_2()
# 	tobo_map.tree_3()
# 	tobo_map.tree_4()

# 	tobo_map.multiply()