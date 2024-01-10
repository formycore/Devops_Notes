"""
_ before data and method to declare protected
"""
class Parent:
    _protectData = 10
    def protectedMethod(self):
        print(self._protectData)
class Child(Parent):
    def method(self):
        print(self._protectData)


# Accessing the class and methods
        
obj1 = Parent()
obj1.protectedMethod() # output is 10
obj2 = Child()
obj2.method() # output is 10 

print(obj1._protectData) # output is 10 

