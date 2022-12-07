"""
Class: callable __call__
"""

class A:
    """Class A, displaying Arguments"""

    def __init__(self):
        print("An instance of A was initialized")

    def __del__(self):
        print("object__Deleted")
    
    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)
              
print(A.__doc__)
x = A() #creating Object x
print(x.__doc__)

print("\nCalling the instance:")
x(3, 4, x=11, y=10)

print("Let's call it again:")
x(3, 4, x=11, y=10)

d = A()
print(d.__doc__)
 """
Class: inheritance
"""

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print("Calling parent constructor")

   def parentMethod(self):
      print('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print("Calling child constructor")

   def childMethod(self):
      print('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
