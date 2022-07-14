<<<<<<< HEAD
import csv
req_file="D:\\DevopS_giT\\Udemy\\python\\15-Working with csv\\new_info.csv"
fo=open(req_file,"r")
content=csv.reader(fo,delimiter="|")
#print(content)
for each in content:
	print(each)
=======
import csv
req_file="D:\\DevopS_giT\\Udemy\\python\\15-Working with csv\\new_info.csv"
fo=open(req_file,"r")
content=csv.reader(fo,delimiter="|")
#print(content)
for each in content:
	print(each)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
fo.close()	