"""
output will be error
"""


class Employee:
    __salary = 30000
    def getBalance(self):
        print(self.__salary)
    def __changeSalary(self, increment):
        self.__salary += increment

class Manager(Employee):
    self.__changeSalary(10000)

obj1 = Manager()
obj1.getBalance()