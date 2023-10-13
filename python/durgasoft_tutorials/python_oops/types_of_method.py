class Student:
	schoolname='maanya' # this is static variable
	def __init__(self,name,rno):
		self.name = name # instance variable
		self.rno = rno   # instance variable
	def getStudentInfo(self):
		print("Student name", self.name) # self.name is instance variable used inside the method, it is instance method
		print("Student rno", self.rno) # self.rno is instance variable used inside the method,it is instance method
	@classmethod
	def getSchoolName(cls):
	    # cls, in python for every class 1 special object class is created, to hold the class level info
	    # here in this cls is reference variable to class level object 
	    print("schoolname is : ", cls.schoolname)
	@staticmethod
	def sum(a,b):
		sum = a+b
		return sum


# Create an instance of the student class
student = Student("arnold", 29)

#Print the values of instance variables
print("Student Name: ", student.name)
print("Student rno: ", student.rno)

# Print the value of static variables
print("schoolname: " ,Student.schoolname)

# print the value of class method
Student.getSchoolName()

# Call the static method
sum = Student.sum(1,2)
print("sum", sum)
