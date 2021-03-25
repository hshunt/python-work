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

	def tree(self):
		x = 0
		trees = 0
		for line in self.map_data:
			string = line[0]
			if string[x] == "#":
				trees+=1
			x+=3
			if x >= len(string):
				x = x - len(string) 
		print(trees)



with open('f:\\Documents\\GitHub\\python-work\\Advent_of_code\\aoc_day3\\input.txt', 'r') as maps:
	tobo_map = Maps(maps)
	# tobo_map.show_map()
	tobo_map.tree()
