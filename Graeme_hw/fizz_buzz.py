def fizzbuzz(nums):

	for number in nums:

		if number % 15 == 0:
			print("FIZZBUZZ")
		elif number % 5 == 0:
			print("BUZZ")
		elif number % 3 == 0:
			print("FIZZ")
		else:
			print(number)

nums = [1,2,3,4,5,6,7,8,9,15]

fizzbuzz(nums)