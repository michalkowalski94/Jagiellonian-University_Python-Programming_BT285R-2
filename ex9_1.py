#open this script with arguments "1" and "two"
#script should be able print stings and integers
#define function that will check if input is an integer
#assign int or str if string or if integer
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
	for i in args:
		if is_number(i) is True:
			number = int(i)
		else:
			string = str(i)
	print "Defining what is a number or string"
	print number, type(number)
	print string, type(string)
