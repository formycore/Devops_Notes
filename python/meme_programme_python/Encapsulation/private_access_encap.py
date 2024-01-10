"""
__ (double underscore) before data and methods to declare private
if the data is private it is accessed in that class 
"""
class Parent:
    __privateData = 10
    def privateMethod(self):
        print(self.__privateData)

class Child(Parent):
    def method(self):
        print(self.__privateData)

obj1 = Parent()
obj1.privateMethod() # output is 10 
obj2 = Child()
obj2.method()
