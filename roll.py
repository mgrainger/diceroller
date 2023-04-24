
import random
import re
import string

class die:
	
	#sides = [1, 2, 3, 4, 5, 6]
	#sides = {
	#	"1" : 1,
	#	"2" : 2,
	#	"3" : 3,
	#	"4" : 4,
	#	"5" : 5,
	#	"6" : 6,
	#}
	
	sides = []
	#sides = [
	#	{"label": "1", "side" : 1},
	#	{"label": "2", "side" : 2},
	#	{"label": "3", "side" : 3},
	#	{"label": "4", "side" : 4},
	#	{"label": "5", "side" : 5},
	#	{"label": "6", "side" : 6}
	#	]
	die_name = ""
	attributes = []
	last_roll = []
	last_roll_str = ""
	last_roll_int = 0
	die_color = ""
		
	def __init__(self, s=6, name = "", side_labels=[], start_value=1, step_value=1):
		#if name != "" :
		#	self.die_name = name
		#self.label = "Test"
		#create_die(self, s, side_labels, start_value=1, step_value=1)
		self.set_name(name)
		#self.set_sides(s)
		#If no values are set for side lables, default to integer lables.
		if len(side_labels) == 0:
			default_labels = True
		else:
			default_labels = False
		


		die_sides = [] #array to store die sides
		for side in range(start_value, s+1, step_value):
			if default_labels:
				die_sides.append({"label": str(side), "side": side})
			else:
				die_sides.append({"label": side_labels[side], "side": side})
		self.set_sides(die_sides)


	#def __init__(self, side_label, side_num, l=""):
	#	self.sides[side_label] = side_num
	#	self.label = l
		#self.attributes = a
	def create_die(self, s, side_labels, start_value, step_value):
		#For each side of the die...
		for ctr in s:
			set_sides()

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
	
	def get_last_roll_int(self):
		return self.last_roll[0].get("side")
	
	def get_last_roll_str(self):
		return self.last_roll[0].get("label")
		
	def roll_die (self):
		return self.set_last_roll(self.sides[random.randint(0, len(self.sides)-1)])
		
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
		print("================================================")
		print("Die Name: " + self.die_name)
		print("Die Attriburtes: " + str(self.attributes))
		print("Die Sides: " + str(self.sides))
		print("Last Roll: " + str(self.last_roll))
		print("Last Roll (str): " + str(self.last_roll_str))
		print("Last Roll (int): " + str(self.last_roll_int))
		
	
	
class dicepool:
	
	dice_pool = [] #stores diece objects
	label = ""     # Name of the dice pool
	last_roll = []
	bonus = 0      #Positive or negative integer value.
	
	def __init__(self, equation, l=""):
		
		self.label = l
		self.createDice(equation)
	
	def __del__(self):
		#del self.dice_pool
		#del self.label
		#del self.last_roll
		#del self.bonus
		pass
	
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
		for die in self.dice_pool:
			this_roll = die.roll()["side"]
			total_roll.append(this_roll)
			#print this_roll
		this_roll += self.bonus
		last_roll = this_roll
		return total_roll
		
	def addDie(self, d):
		self.dice_pool.append(d)
	
	def removeDie(self):
		self.dice_pool.pop()
		
	def removeDice(self):
		del dice_pool
	
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
		parsed = re.findall("[+-]*(\d+[dD]+\d+)", dicestring)
		for dice_equation in parsed: #Try replacing this with parseDice
			temp = re.search("(\d+)[dD]+\d+", dice_equation)
			print("temp = " + str(temp.group(1)))
			num_dice = int(temp.group(1))
			num_sides = int(re.search("\d+[dD]+(\d+)", dice_equation).group(1))
			print("num_sides = " + str(num_sides))
			num_range = range(1, num_sides+1)
			print("num_range = " + str(num_range))
			for dice in range(num_dice):
				#newDie = die(num_range)
				die_sides = []
				for side in range(num_sides):
					die_sides.append({"label": str(side), "side": side})
				newDie = die(die_sides)
				self.addDie(newDie)
	
def parseDice(self, dicestring):
	#this parses dice equations in the form of #d#+#. Returns a dict list of the three values.
	parsed = re.findall("[+-]*(\d+[dD]+\d+)", dicestring)
	
	
def main():
	
	user_input = ""
	#myDice = dicepool()
	dicebag = [] #Storage for multiple dice pool objects.
	
	while user_input != "exit":
		
		user_input = input("[&]: ")
		split_input = user_input.split()  #string.split(user_input)
		
		if user_input == "":
			continue
		elif split_input[0] == "quit" or split_input[0] == "q": 
			break
		elif split_input[0] == "clear":
			dicebag = []
		elif split_input[0] == "new":
			#newPool = dicepool(split_input[2], split_input[1])
			dicebag.append(dicepool(split_input[2], split_input[1]))
			print("New dice pool " + split_input[1] + " created.")
			
		elif split_input[0] == "print":
			for pool in dicebag:
				pool.printDicePool()
		
		elif split_input[0] == "roll":
			#If formmatted correctly
			if re.match("\d+[dD]\d+[\+-]*\d*", split_input[1]):
				quickPool = dicepool(split_input[1], "QuickPool")
				print(str(quickPool.rollPool()))
				#quickPool.removeDice()
				#del quickPool
			else:
				for pool in dicebag:
					if pool.label == split_input[1]:
						print(str(pool.rollPool()))
		
		elif split_input[0] == "get":
			# get <lable> label
			# get <label> lastroll
			pass
		elif split_input[0] == "help":
			print("-= COMMANDS =-")
			print("quit : ends the program")
			print("clear : clears the dicebag")
			print("new : create a new named dicebag ex. \'new <dice> <label>\'")
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