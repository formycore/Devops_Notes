<<<<<<< HEAD
'''from random import choice
len_pass=8
valid_chars="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?"
print(choice(valid_chars))
# I need 8 chars in my password
passwd=[]
for each_char in range(len_pass):
    print(choice(valid_chars))'''


from random import choice
len_pass=8
valid_chars="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?"
passwd=[]
random_pass="".join(choice(valid_chars) for each_char in range(len_pass))
=======
'''from random import choice
len_pass=8
valid_chars="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?"
print(choice(valid_chars))
# I need 8 chars in my password
passwd=[]
for each_char in range(len_pass):
    print(choice(valid_chars))'''


from random import choice
len_pass=8
valid_chars="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?"
passwd=[]
random_pass="".join(choice(valid_chars) for each_char in range(len_pass))
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print(random_pass)