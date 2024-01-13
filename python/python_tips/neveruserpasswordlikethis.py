# pwd = input('Password: ')
# print('you typed: ', pwd)
"""
The above command will print the password and echo's it
it is vunerablity/security practice
to over come this 

Taking the password in the terminal 
import getpass 
"""
from getpass import getpass

pwd = getpass('Password: ')

print("you typed the password: ", pwd)

"""
While typing the password it will not show the password that we typed in 
just like ansible private while typing the password 

"""