# lambda functions
# In this approach, we use lambda() function, to calculate the area by multiplying the given length and width. Lambda functions are concise, anonymous functions that can be handy for short-lived operations
from functools import reduce
def area_of_rectangle(length, width):
    return reduce(lambda x, y: x * y , [length, width] )
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
result = area_of_rectangle(length, width)
print(f"Area of rectangle: " , result)