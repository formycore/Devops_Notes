<<<<<<< HEAD
from random import choice
len_of_passwd=8
valid_chars_for_passwd="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?"
#print(choice(valid_chars_for_passwd))
passwd=[]
'''
for each in range(len_of_passwd):
    passwd.append(choice(valid_chars_for_passwd))
random_pass="".join(passwd)
print(random_pass)
'''
random_pass="".join(choice(valid_chars_for_passwd)for each_char in range(len_of_passwd))
=======
from random import choice
len_of_passwd=8
valid_chars_for_passwd="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?"
#print(choice(valid_chars_for_passwd))
passwd=[]
'''
for each in range(len_of_passwd):
    passwd.append(choice(valid_chars_for_passwd))
random_pass="".join(passwd)
print(random_pass)
'''
random_pass="".join(choice(valid_chars_for_passwd)for each_char in range(len_of_passwd))
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print(random_pass)