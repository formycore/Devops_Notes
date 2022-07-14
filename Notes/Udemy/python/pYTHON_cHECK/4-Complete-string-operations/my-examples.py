<<<<<<< HEAD
import os
import crypt

password ="p@ssw0rd" 
encPass = crypt.crypt(password,"22")
=======
import os
import crypt

password ="p@ssw0rd" 
encPass = crypt.crypt(password,"22")
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
os.system("useradd -p "+encPass+" johnsmith")