
import random
import re
import string

class die:
		
	def __init__(self, s=6, name = "", side_labels=[], start_value=1, step_value=1):
		self.sides = []
		self.die_name = name
		self.last_roll = []
		self.last_roll_label = ""
		self.last_roll_side = 0
		self.die_color = ""
		
		self.set_name(name)
		
		for side in range(start_value, s+1, step_value):
			if len(side_labels) == 0:
				self.sides.append({"label": str(side), "side": side})
			else:
				self.sides.append({"label": side_labels[side], "side": side})

	#Takes in a dictionary object.
	def set_sides(self, s=[]):
		self.sides = s
		return self.sides
		
	def set_name(self, l=""):
		self.die_name = l
		return self.die_name
	
	def get_name(self):
		return self.die_name
	
	def set_last_roll(self, lr=[]):
		self.last_roll = lr
		return self.last_roll	
	
	def get_last_roll_side(self):
		return self.last_roll[0].get("side")
	
	def get_last_roll_label(self):
		return self.last_roll[0].get("label")
		
	def roll_die (self):
		return self.set_last_roll(self.sides[random.randint(0, len(self.sides)-1)])
		
	def printInfo(self):
		print("================================================")
		print("Die Name: " + self.die_name)
		#print("Die Attriburtes: " + str(self.attributes))
		print("Die Sides: " + str(self.sides))
		print("Last Roll: " + str(self.last_roll))
		print("Last Roll (label): " + self.last_roll_label)
		print("Last Roll (side): " + str(self.last_roll_side))

	
class dicepool:
	
	def __init__(self, equation, label=""):
		
		self.dice_pool = [] #stores dice objects
		self.label = label     # Name of the dice pool
		self.last_roll = []
		self.bonus = 0      #Positive or negative integer value.
		self.createDice(equation)
		self.dice_equation = equation
		
	def sum(self, rolls):
		return sum(rolls)
	
	def average(self, rolls):
		pass
	
	def halfd(self):
		pass
		
	def halfu(self):
		pass
	
	def rollPool(self):
		this_roll = 0
		total_roll = []
		total_roll.clear
		for die in self.dice_pool:
			this_roll = die.roll_die()["side"]
			total_roll.append(this_roll)
			#print this_roll
		#this_roll += self.bonus
		self.last_roll = total_roll
		#return sum(total_roll)+self.bonus
		#return total_roll
		return sum(total_roll)+self.bonus
		
	def addDie(self, d):
		self.dice_pool.append(d)
	
	def removeDie(self):
		self.dice_pool.pop()
		
	def removeDice(self):
		del self.dice_pool
	
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
			print(die.printInfo())
	
	def getLastRoll(self):
		return self.last_roll
		
	def printLastRoll(self):
		for roll in self.last_roll:
			print(roll)

	def createDice(self, dicestring):
		#num_dice = 0
		#num_sides = 0
		
		#self.bonus = int(re.search("([\+-]+\d+)\s", dicestring))
		parsed = re.findall("(\d+[dD]+\d+[+-]*\d*)", dicestring)
		temp_bonus = 0
		for dice_equation in parsed: #Try replacing this with parseDice
			#temp = re.search("(\d+)[dD]+\d+", dice_equation)
			#print("temp = " + str(temp.group(1)))
			num_dice = int(re.search("(\d+)[dD]+\d+[+-]*\d*", dice_equation).group(1))
			print("num_dice = " + str(num_dice))
			num_sides = int(re.search("\d+[dD]+(\d+)[+-]*\d*", dice_equation).group(1))
			print("num_sides = " + str(num_sides))
			bonus_check = re.search("\d+[dD]+\d+([+-]*\d*)", dice_equation).group(1)
			if bonus_check != '':
				temp_bonus += int(bonus_check)
				#num_range = range(1, num_sides+1)
			#print("num_range = " + str(num_range))
			for dice in range(num_dice):
				#newDie = die(num_range)
				#die_sides = []
				#for side in range(num_sides):
				#	die_sides.append({"label": str(side), "side": side})
				newDie = die(num_sides)
				self.addDie(newDie)
		self.bonus = temp_bonus
	
def parseDice(self, dicestring):
	#this parses dice equations in the form of #d#+#. Returns a dict list of the three values.
	return re.findall("[+-]*(\d+[dD]+\d+)", dicestring)
	
	
def main():
	
	user_input = ""
	#myDice = dicepool()
	dicebag = [] #Storage for multiple dice pool objects.
	current_pool = 0
	loaded_dicepool = dicepool("", "&")
	
	while user_input != "exit":
		
		user_input = input("[" + loaded_dicepool.label + "]: ")
		split_input = user_input.split()  #string.split(user_input)
		
		if user_input == "":
			continue
		elif split_input[0] == "quit" or split_input[0] == "q": 
			break
		elif split_input[0] == "clear":
			loaded_dicepool = dicepool("", "&")
			dicebag = []
		elif split_input[0] == "create":
			#newPool = dicepool(split_input[2], split_input[1])
			dicebag.append(dicepool(split_input[1], split_input[2]))
			print("New dice pool " + split_input[2] + " with " + split_input[1] + " created.")
			
		elif split_input[0] == "print":
			for pool in dicebag:
				print(pool.label + "  " + pool.dice_equation)
				#pool.printDicePool()
		
		elif split_input[0] == "load":
			for pool in dicebag:
				if pool.label == split_input[1]:
					loaded_dicepool = pool
					break
				else:
					print("Dice pool not found")

		elif split_input[0] == "roll":
			#If formmatted correctly
			if len(split_input) == 1:
				print(str(loaded_dicepool.rollPool()))
				#print ("Please enter a dice equation or dice pool name to roll.")
			elif re.match("\d+[dD]\d+[\+-]*\d*", split_input[1]):
				quickPool = dicepool(split_input[1], "QuickPool")
				print(str(quickPool.rollPool()))
				#quickPool.removeDice()
				del quickPool
			else:
				for pool in dicebag:
					if pool.label == split_input[1]:
						total = pool.rollPool()
						print(str(pool.last_roll) + "+" + str(pool.bonus) + " = " + str(total))
		
		elif split_input[0] == "get":
			# get <lable> label
			# get <label> lastroll
			pass
		elif split_input[0] == "help":
			print("-= COMMANDS =-")
			print("quit : ends the program")
			print("clear : clears the dicebag")
			print("create : create a new named dicebag ex. \'create <dice> <label>\'")
			print("roll : roll the dice indicated. ex. \'roll <dice>\'")
		elif split_input[0] == "test":
			testDie = die(6) #Create Dice Object
			#testDie.createDie()

			print(testDie.roll_die()["side"])
			#testDie.set_sides([{"label": "1", "side" : 1}, {"label": "2", "side" : 2}, {"label": "3", "side" : 3}, {"label": "4", "side" : 4}])
			testDie.printInfo()



		parsed = re.findall("[+-]*(\d+)[dD]+(\d+)", user_input)
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
		
		#print str(dicebag[0].rollPool())

	
	
if __name__== "__main__":
	main()