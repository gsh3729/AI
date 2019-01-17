class Agent:
	direction=1   #direction 1 is for right, 0 is for left
	steps=1 	

	def walking(self):
		while percept.checkingShore():
			if self.direction:
				percept.current_location=percept.current_location+self.steps
				self.direction=0

			else:
				percept.current_location=percept.current_location-self.steps
				self.direction=1

			self.steps+=1

			print "Bunny location - ",percept.current_location,"\tAction steps - ",self.steps,"\tDirection - ",
			if self.direction:
				print "Right"
			else:
				print "Left"

		print "Shore is reached"

class Environment:
	current_location=6
	shore_location=13

	def checkingShore(self):
		if self.current_location == self.shore_location : 
			return 0
		else :
			return 1

percept = Environment()
a = Agent()
a.walking()


			

		
	 			