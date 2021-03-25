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
	result = 0

	for num in nums:
		x = len(nums)
		x = x-1
		while result != 2020:
			result = num + nums[x]
			if x < 0:
				break
			if result == 2020:
				answer = num * nums[x]
				print(answer)
			x = x-1
			
# find max and min of list in one for loop
def m_m(nums):
	x = len(nums)
	x = x-1
	min_num = 10000
	max_num = 1

	for num in nums:
		if num > nums[x]:
			if max_num < num:
				max_num = num
		elif num < nums[x]:
			if min_num > num:
				min_num = num
		x-1

	print(f"The max of the list is {max_num} and the min of the list is {min_num}")

nums = make_list(ep_nums)
num_find(nums)
