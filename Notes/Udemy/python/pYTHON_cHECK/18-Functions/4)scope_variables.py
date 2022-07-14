<<<<<<< HEAD
# python gives more prirority for local variables
def myfun1():
	x=60 # local variable
	print("Welcome to functions")
	print("x value is:",x)
	#myfun2()
	return None
def myfun2(y): # here the y is called PARAMETER
	print("Thank you")
	print("y value from the fun2 is:",y)
	return None
#x=60 global function
def main(): # code starts from here
	global x
	x=10 
	myfun1()
	myfun2(x) # here the x is called ARGUMENT
	return None
=======
# python gives more prirority for local variables
def myfun1():
	x=60 # local variable
	print("Welcome to functions")
	print("x value is:",x)
	#myfun2()
	return None
def myfun2(y): # here the y is called PARAMETER
	print("Thank you")
	print("y value from the fun2 is:",y)
	return None
#x=60 global function
def main(): # code starts from here
	global x
	x=10 
	myfun1()
	myfun2(x) # here the x is called ARGUMENT
	return None
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
main()	