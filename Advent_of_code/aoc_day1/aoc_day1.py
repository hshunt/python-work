ep_1 = open('f:\\Documents\\GitHub\\python-work\\Advent_of_code\\aoc_day1\\ep_nums.txt', 'r')
ep_2 = open('f:\\Documents\\GitHub\\python-work\\Advent_of_code\\aoc_day1\\ep_nums.txt', 'r')
ep_nums_1 = ep_1.readlines()
ep_nums_2 = ep_2.readlines()
ep_1.close()
ep_2.close()

def make_list(nums):
	nums_fixed = []
	for num in nums:
		stripped_num = num.strip("\n")
		nums_fixed.append(int(stripped_num))
	return nums_fixed


def num_find(nums_1, nums_2):
	for num_1 in nums_1:
		for num_2 in nums_2:
			if num_1 + num_2 == 2020:
				answer = num_1 * num_2
				print(answer)

# class Nums():
# 	nums_fixed = []


# 		for num in nums:
# 			stripped_num = num.strip("\n")
# 			self.nums_fixed.append(int(stripped_num))
# 		return self.nums_fixed



nums_1 = make_list(ep_nums_1)
nums_2 = make_list(ep_nums_2)
print(nums_1)
print(nums_2)
num_find(nums_1, nums_2)