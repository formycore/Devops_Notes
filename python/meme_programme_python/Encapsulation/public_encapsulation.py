class Parent:
    publicData = 10
    def publicMethod(self):
        print(self.publicData)
class Child(Parent):
    def method(self):
        print(self.publicData)

# now accessing the public data
obj1 = Parent()
obj1.publicMethod() # output is 10
print(obj1.publicData) # output is 10

obj2 = Child()
obj2.method() # output is 10
print(obj2.publicData) # output is 10 

