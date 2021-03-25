ep = open('f:\\Documents\\GitHub\\python-work\\Advent_of_code\\aoc_day1\\ep_nums.txt', 'r')
ep_nums = ep.readlines()
ep.close()

def make_list(nums):
	nums_fixed = []
	for num in nums:
		stripped_num = num.strip("\n")
		nums_fixed.append(int(stripped_num))
	return nums_fixed

def num_find(nums):
	result = 2020
	x = len(nums)
	x = x-1
	y = 0

	for num in nums:
		cont = True
		while cont == True:
			while y < len(nums):
				result = num + nums[x] + nums[y]
				if result == 2020:
					answer = num * nums[x] * nums[y]
					print(answer)
					break
					cont = False
				y = y + 1
			if x > 0:
				x = x - 1
				y = 0
			else:
				cont = False
				x = len(nums)
				x = x-1
			if result == 2020:
				break
		if result == 2020:
			break
nums = make_list(ep_nums)
num_find(nums)