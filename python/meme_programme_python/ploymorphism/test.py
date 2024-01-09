class A:
    def method1(self):
        print("This is parent class")
class B(A):
    def method1(self):
        print("This is child class")

obj = A ()
obj.method1()
