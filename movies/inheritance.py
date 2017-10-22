class Parent():
	def __init__(self, last_name, eye_color):
		self.last_name = last_name
		self.eye_color = eye_color

#the argument here indicates that child inherits from parent
class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		#initialize the child variables using the parent methods
		Parent.__init__(self,last_name, eye_color)
		#declare the new instance variable that is not present in the parent class
		self.number_of_toys = number_of_toys