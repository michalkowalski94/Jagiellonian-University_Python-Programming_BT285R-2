# TEST1: Create a scipt that will get input from command line and decide whether it is a string or integer
def is_number(var):
	"""This function is testing if variable is a number with
		returning True or False"""
	try:
		if int(var) or int(var)==0:
			return True
	except Exception:
        	return False

if __name__ == '__main__':
	import sys
	print('program: %s' %sys.argv[0])
	for arg in sys.argv[1:]:
		print('Arg: %s' %arg)
		print type(arg)
	args = sys.argv[1:]
	variables = []
	for i in args:
		if is_number(i) is True:
			number = int(i)
			variables.append(number)
		else:
			string = str(i)
			variables.append(string)
	print "Defining what is a number or string"
	for i in variables:
		print i, type(i)
