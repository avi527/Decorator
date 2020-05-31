'''the decorators will be applied in the order that we've called them. Below we'll 
define another decorator that splits the sentence into a list. 
We'll then apply the uppercase_decorator and split_string decorator to a single function.'''

def splitString(function):
	def wrapper():
		fun=function()
		funSplit=fun.split()
		return funSplit
	return wrapper

def UpperCase(function):
	def wrapper():
		f=function()
		uppCaseF=f.upper()
		return uppCaseF
	return wrapper


@splitString
@UpperCase
def saySomthing():
	return "hello how are you"
print(saySomthing())

