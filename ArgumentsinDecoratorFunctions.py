'''Sometimes we might need to define a decorator that accepts arguments. 
We achieve this by passing the arguments to the wrapper
 function. The arguments will then be passed to the function that is being decorated at call time.'''

def argumentDecorater(function):
	def argumentWrapper(city1,city2):
		print("My arguments are: {0}, {1}".format(city1,city2))
		function(city1, city2)
	return argumentWrapper

@argumentDecorater
def Cities(c1,c2):
 	print("my first fav city is {} and second is {}".format(c1,c2))
Cities('Delhi','Bhopal')


#Defining General Purpose Decorators
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()