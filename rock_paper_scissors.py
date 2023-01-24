class rps():
	def __init__(self):
		self.rock = "rock"
		self.paper = "paper"
		self.scissors = "scissors"

	def user1(self):
		self.user1_input = input("[User1] Please enter a choose: ")

	def user2(self):
		self.user2_input = input("[User2] Please enter a choose: ")

	def gamerun(self):
		if self.user1_input == self.rock:
			if self.user2_input == self.rock:
				print("Scroless!")
			elif self.user2_input == self.paper:
				print("Paper won!")
			elif self.user2_input == self.scissors:
				print("Rock won!")

		elif self.user1_input == self.paper:
			if self.user2_input == self.paper:
				print("Scroless!")
			elif self.user2_input == self.rock:
				print("Paper won!")
			elif self.user2_input == self.scissors:
				print("Scissors won!")

		elif self.user1_input == self.scissors:
			if self.user2_input == self.scissors:
				print("Scroless!")
			elif self.user2_input == self.paper:
				print("Scissors won!")
			elif self.user2_input == self.rock:
				print("Rock won!")

		elif self.user2_input == self.rock:
			if self.user1_input == self.rock:
				print("Scroless!")
			elif self.user1_input == self.paper:
				print("Paper won!")
			elif self.user1_input == scissors:
				print("Rock won!")

		elif self.user2_input == self. paper:
			if self.user1_input == self.paper:
				print("Scroless!")
			elif self.user1_input == self.rock:
				print("Paper won!")
			elif self.user2_input == self.scissors:
				print("Scissors won!")

		elif self.user2_input == self.scissors:
			if self.user1_input == self.scissors:
				print("Scroless!")
			elif self.user1_input == self.paper:
				print("Scissors won!")
			elif self.user1_input == self.rock:
				print("Rock won!")

my_instance = rps()
my_instance.user1()
my_instance.user2()
my_instance.gamerun()