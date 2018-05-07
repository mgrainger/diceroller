
import random
import re

class die:
	
	def __init__(self, x, low=1):
		sides = x
	
	def roll (sel):
		return random.randint(low, sides)
		
		
		#for die in range(dice):
			#results.append(randint(1, sides))
			
		#return
	
class dice:
	
	self.dice_pool = []
	
	def __init__(self, d_pool):
		self.dice_pool = d_pool
	
	def sum(self, rolls):
		return sum(rolls)
	
	def average(self, rolls):
		return average(rolls)
	
	def rollpool(self):
		for die in self.dice_pool:
			die.roll()
		
	
	
def main():
	input = raw_input("Enter dice to roll: ")
	parsed = re.findall("(\d+)[dD]+(\d+)", input)
	#print input
	#print parsed
	#print args
	
	myDie = die()
	myDie.roll(int(parsed[0][0]), int(parsed[0][1]))
	
	
	
	
if __name__== "__main__":
	main()