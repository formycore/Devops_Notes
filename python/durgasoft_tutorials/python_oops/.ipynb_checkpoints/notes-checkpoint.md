```
Python oops

Before oops there was a pop
Pop is call procedure Oriental programming or function or enter programming
Here we need to mainly focus on three aspects
That is class , object , a reference variable
To understand clearly what is class means we need to go with an example 

Example one building plan
First we need to contact the architecture he will provide the plan now with that plan we will go to contact the builder builder will fill the building

With same plan we can Bangalore Chennai Hyderabad

Here we have only one plan and there are three buildings

Here in the example we can take plan as a class

We can also take class as a die and object as an output



Physical existence of any class is called object

Class acts as blueprint/plan/model/design for the objects hearing the example class is a plan


Object  a physical existence of an class here in the example buildings are objects


How to define a classs
class name_of_the_class:
  ''' documentation string'''
  properties (variables)
  methods (functions/actions)
###################################################################
class Student:
    '''This is a student class with required data'''
    # variables or properties (like name, age, marks, etc)
    # methods or actions (like study, play, etc)
    print(student.__doc__)
    help(student)
###################################################################
- we can use this doc string for documentation purpose
- every object will have properties and actions/behaviours
- properties are represented/specified by variables
- actions/behaviours are represented/specified by methods
###################################################################

3 types of variables in python class
------------------------------------
1. Instance variables (object level variables)
2. Static variables (class level variables)
3. Local variables (method level variables)

3 types of methods in python class
----------------------------------
1. Instance methods (object level methods)
2. Static methods (class level methods)
3. Class methods (class level methods)

*****************************************************
**Reference variable**
----------------------
- for a tv remote is required to operate the tv
- here tv is an object and remote is a reference variable
- reference variables can be used to refer the objects by using the reference variable we can access the properties and methods of the object
- we can invoke functionality for single object there can be multiple reference
- if we use functions inside the call it is called method
- HOW TO CREATE AN OBJECT IN PYTHON
- we can create an object by using the following syntax
class_name() # this will create an object
- we can create multiple objects for the same class
- each object is has different id
        print(id(s))
        print(id(s1))
######################################################
class Student:
  def__init__(self):
    print("constructor execution")
    slef.name="sunny"
    self.age=23
    self.marks=80
    def talk(self):
        print("Hello my self:",self.name)
        print("my age is:",self.age)
        print("my marks are:",self.marks)
s = Student()
s1 = Student()
print(s.name)
print(s.age)
print(s.marks)
s.talk()

print(id(s))
print(id(s1))
- here s is a reference variable and Student() is an object
######################################################
def __init__(self): # this is the constructor
- whenever we are creating an object constructor will be executed automatically
- constructor is responsible to declare and initialize the variables
- without constructor can we create an object?
- yes we can create an object without constructor
- if we are not providing any constructor then python will provide default constructor
- what is the purpose of constructor?
- the main purpose of constructor is to declare and initialize the variables
- constructor will execute only once per object
- constructor name should be always __init__(self)
- self is the default variable which is always pointing to current object



data should be changed from object to object then we should go for instance variables






```