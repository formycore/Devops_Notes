<<<<<<< HEAD
import os
import sys
cwd=os.getcwd()
# some non exisiting diretory
fd='C://jio'
# trying to insert the false directory
try:
	os.chdir(fd)
	print("Inserting Inside-",os.getcwd())
# Catching the exception
except:
	print("Something Worng with specified directory",sys.exc_info())
# handling with finally
finally:
	print("Restoring with path")
	os.chdir(cwd)
=======
import os
import sys
cwd=os.getcwd()
# some non exisiting diretory
fd='C://jio'
# trying to insert the false directory
try:
	os.chdir(fd)
	print("Inserting Inside-",os.getcwd())
# Catching the exception
except:
	print("Something Worng with specified directory",sys.exc_info())
# handling with finally
finally:
	print("Restoring with path")
	os.chdir(cwd)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
	print("Current working directory is: ",os.getcwd())