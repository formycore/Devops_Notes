class Mobile:
    def __init__(self,price,modelno):
        self.price = price
        self.modelno = modelno
    def discountPrice(self):
        return self.price-self.price*(1/10) # this is for 10% discount
    def commonmethod1(self):
        return "this is common method1"
    def commonmethod2(self):
        return "This is common method 2"
    def getPrice(self):
        return self.price
    def getModel(self):
        return self.modelno

# now change the discount for only Iphone
class Iphone(Mobile):
    def __init__(self, price, modelno):
        Mobile.__init__(self,price,modelno)
    def somemethod1(self):
        return "This is some method1"
    def somemethod2(self):
        return " This is some method2"
    def discountPrice(self):
        return self.price-self.price*(15/100)
class Samsung(Mobile):
    def __init__(self, price, modelno):
        super().__init__(price, modelno) # when we use super method don't use self 
    def somemethod3(self):
        return "This is some method 3" 
    def somemethod4(self):
        return "This is some method 4"
      
iphone_obj1 = Iphone(50222,1001)
print(iphone_obj1.discountPrice())

samsung_obj2 = Samsung(90000,102)
print(samsung_obj2.discountPrice())