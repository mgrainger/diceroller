
import random
import re

class die:
	
	sides = [1, 2, 3, 4, 5, 6]
		
	def __init__(self, x):
		self.sides = x
	
	def roll_die (self):
		return self.sides[random.randint(1, len(self.sides)-1)]
		
	def roll(self, advantage=False, disadvantage=False):
		if advantage and disadvantage:
			return self.roll_die()
		elif advantage:
			return self.roll_with_advantage()
		elif disadvantage:
			return self.roll_with_disadvantage()
		else:
			return self.roll_die()
	
	def roll_with_advantage(self):
		roll1 = self.roll_die()
		roll2 = self.roll_die()
		return roll1 if roll1 >= roll2 else roll2
		
	def roll_with_disadvantage(self):
		roll1 = self.roll_die()
		roll2 = self.roll_die()
		return roll1 if roll1 <= roll2 else roll2
	
	
class dice:
	
	dice_pool = []
	
	def __init__(self, d_pool):
		self.dice_pool = d_pool
	
	def sum(self, rolls):
		return sum(rolls)
	
	def average(self, rolls):
		return average(rolls)
	
	def rollpool(self):
		for die in self.dice_pool:
			print die.roll()
		
	def adddie(self):
		pass
	
	
	
def main():
	input = raw_input("Enter dice to roll: ")
	parsed = re.findall("(\d+)[dD]+(\d+)", input)
	#print input
	#print parsed
	#print args
	
	die_sides = []
	myDicePool = []
	
	#for side in range(int(parsed[0][1])):
	#	die_sides.append(side)
		
	die_sides = range(int(parsed[0][1]))
	print "die_sides = " + str(die_sides)
	
	for _ in range(int(parsed[0][0])):
		myDie = die(die_sides)
		myDicePool.append(myDie)
	
	print "myDicePool = " + str(myDicePool)
	
	myDice = dice(myDicePool)
	
	#myDie = die()
	#myDie.roll(int(parsed[0][0]), int(parsed[0][1]))
	myDice.rollpool()
	
	
	
if __name__== "__main__":
	main()