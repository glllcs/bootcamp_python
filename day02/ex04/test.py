import ai42
from time import sleep
import time
from random import randint


class CoffeeMachine(): 
	
	water_level = 100

	@ai42.log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!") 
			return False

	@ai42.log
	def boil_water(self): 
		return "boiling..."

	@ai42.log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20): 
				time.sleep(0.1)
				self.water_level -= 1 
			print(self.boil_water()) 
			print("Coffee is ready!")

	@ai42.log
	def add_water(self, water_level): 
		time.sleep(randint(1, 5)) 
		self.water_level += water_level 
		print("Blub blub blub...")


listy = range(3333)
ret = 0
for elem in ai42.ft_progress(listy):
    ret += (elem)
    sleep(.001)
print()
print(ret)

machine = CoffeeMachine() 
for i in range(0, 5):
    machine.make_coffee()
machine.make_coffee()
machine.add_water(70)