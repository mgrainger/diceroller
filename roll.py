
import random
import re
import string

class die:
	
	sides = [1, 2, 3, 4, 5, 6]
	label = ""
	attributes = []
	last_roll = ""
		
	def __init__(self, s, l="", a=[]):
		self.sides = s
		self.label = l
		self.attributes = a
	
	def roll_die (self):
		return self.sides[random.randint(0, len(self.sides)-1)]
		
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
	
	def printInfo(self):
		print "================================================"
		print "Die Label: " + str(self.label)
		print "Die Attriburtes: " + str(self.attributes)
		print "Die Sides: " + str(self.sides)
		
	
	
class dicepool:
	
	dice_pool = []
	label = ""
	last_roll = []
	bonus = 0
	
	def __init__(self, equation, l=""):
		
		self.label = l
		self.createDice(equation)
	
	def sum(self, rolls):
		return sum(rolls)
	
	def average(self, rolls):
		return average(rolls)
	
	def halfd(self):
		pass
		
	def halfu(self):
		pass
	
	def rollPool(self):
		total_roll = []
		for die in self.dice_pool:
			this_roll = die.roll()
			total_roll.append(this_roll)
			#print this_roll
		this_roll += self.bonus
		last_roll = this_roll
		return total_roll
		
	def addDie(self, d):
		self.dice_pool.append(d)
	
	def removeDie(self):
		self.dice_pool.pop()
	
	def removeDieByLabel(self, xlabel):
		for index, die in enumerate(self.dice_pool):
			if die.label == xlabel:
				del self.dice_pool[index]
				break #remove die
		
				
	
	def removeDieByType(self):
		pass
		
	def removeDieByAttribute(self):
		pass
		
	def printDicePool(self):
		for die in self.dice_pool:
			print die.printInfo()
	
	def getLastRoll(self):
		return self.last_roll
		
	def printLastRoll(self):
		for roll in self.last_roll:
			print roll

	def createDice(self, dicestring):
		#num_dice = 0
		#num_sides = 0
		
		#self.bonus = int(re.search("([\+-]+\d+)\s", dicestring))
		parsed = re.findall("[+-]*(\d+[dD]+\d+)", dicestring)
		for dice_equation in parsed:
			temp = re.search("(\d+)[dD]+\d+", dice_equation)
			print "temp = " + str(temp.group(1))
			num_dice = int(temp.group(1))
			num_sides = int(re.search("\d+[dD]+(\d+)", dice_equation).group(1))
			print "num_sides = " + str(num_sides)
			num_range = range(1, num_sides+1)
			print "num_range = " + str(num_range)
			for _ in range(num_dice):
				newDie = die(num_range)
				self.addDie(newDie)
	
	
def main():
	
	input = ""
	#myDice = dicepool()
	dicebag = [] #Storage for multiple dice pool objects.
	
	while input != "exit":
		
		input = raw_input("[>]: ")
		split_input = string.split(input)
		
		if split_input[0] == "exit": 
			break
		elif split_input[0] == "clear":
			pass
		elif split_input[0] == "new":
			newPool = dicepool(split_input[2], split_input[1])
			dicebag.append(newPool)
			print "New dice pool " + split_input[1] + " created."
			
		elif split_input[0] == "print":
			pass
		
		elif split_input[0] == "roll":
			pass
		
		parsed = re.findall("[+-]*(\d+)[dD]+(\d+)", input)
		#print input
		#print parsed
		#print args
		
		#die_sides = []
		#myDicePool = []
		
		
		#for side in range(int(parsed[0][1])):
		#	die_sides.append(side)
			
		#die_sides = range(1, int(parsed[0][1])+1)
		#print "die_sides = " + str(die_sides)
		
		#for num in range(int(parsed[0][0])):
		#	currentDie = die(die_sides, "Die" + str(num), ["Damage", "Radiant"])
		#	myDice.addDie(currentDie)
		
		#print "myDice = " + str(myDicePool)
		
		#myDice = dicepool(myDicePool)
		
		#myDie = die()
		#myDie.roll(int(parsed[0][0]), int(parsed[0][1]))
		#print str(myDice.rollPool())
		#myDice.printDicePool()
		
		print str(dicebag[0].rollPool())
	
	
if __name__== "__main__":
	main()