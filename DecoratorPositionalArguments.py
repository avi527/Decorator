#use the decorator using positional arguments.
def DataValeDeco(function):
	def exceptArgument(*arg,**kwargs):
		print('The positional arguments are', arg)
		print('The keyword arguments are', kwargs)
		function(*arg,**kwargs)
	return exceptArgument

@DataValeDeco
def DataValue(a,b,c):
	print(a,b,c)
DataValue(2,6,8)
