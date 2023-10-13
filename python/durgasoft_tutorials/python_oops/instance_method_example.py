class Test:
	@classmethod
	def m1(cls):
		print(id(cls))

print(id(Test))
Test.m1()