# DEFINITIONS
class MyException(Exception):
	def __init__(self):
		pass
			
	def __str__(self):
		return ('Found the symbol # from the input string!')

def get_name():
	print("Please enter a name (if it contains a '#', an error message will appear: ")
	name_input = input()
	if name_input.find('#') > -1:
		raise(MyException)

# EXECUTION

try:
	get_name()
except MyException:
	print(MyException().__str__())