class Parent():
	"""docstring for ."""
	def __init__(self):
		self.greeting = "Hi, I'm a parent object."
	def __str__(self):
		return self.greeting
 
class ChildA(Parent):
	"""docstring for ."""
	def __init__(self):
		self.greeting = "Hi, I'm a child object."
	def __str__(self):
		return self.greeting
 
class ChildB(Parent):
	pass

# Init a Parent object and return "greeting"
parentObj = Parent()
print(parentObj.__str__())
 
# Init a ChildA object and return "greeting"
childAObj = ChildA()
print(childAObj.__str__())
 
# Init a ChildB object and return "greeting"
childBObj = ChildB()
print(childBObj.__str__())