class Passwords():
	def __init__(self, pws):
		self.pw = []
		self.cnt = 0
		for line in pws:
			l = line.replace("-", " ").replace(":","").split()
			l = (l[0], l[1], l[2], (l[3],))
			self.pw.append(l)
			self.cnt += 1
		print(self.pw)
		

	def count(self, cnt, cl_list,):
		cl_cnt = 0
		for line in cl_list:
			cl_cnt +=1
		if cnt == cl_cnt:
			print("The count is correct")
		else:
			print(f"Count error: cnt = {cnt}, and the class count = {cl_cnt}")
	
	def pw_check(self):
		valid_pw = 0

		for self.password in self.pw:
			r_0 = int(self.password[0])
			r_1 = int(self.password[1])
			r_2 = self.password[2]
			r_0 -= 1
			r_1 -= 1
			pw_tup = self.password[3][0]
			if r_2 == pw_tup[r_0] and r_2 == pw_tup[r_1]:
				continue
			elif r_2 == pw_tup[r_0] or r_2 == pw_tup[r_1]:
				valid_pw += 1
		print(valid_pw)


with open('f:\\Documents\\GitHub\\python-work\\Advent_of_code\\aoc_day2\\passwords.txt', 'r') as passwords:

	pw_db = Passwords(passwords)
	pw_db.count(pw_db.cnt, pw_db.pw)
	pw_db.pw_check()

