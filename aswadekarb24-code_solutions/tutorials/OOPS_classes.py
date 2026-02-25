# OOPS in Python
# To map with real world scenarios, we started using objects in the code
# This is called object oriented programming

# Class & Objects in Python
# Class is a blueprint for creating objects

class Car():
    color="Red"
    brand="Mercedes"

c1=Car()
print(c1.color)
print(c1.brand)

# Constructor or __init__ function
# All classes have a function __init(), which is always executed when the class is being initiated.

class Student():

    # Default constructors
    def __init__(self):
        pass

    # Parameterized constructors
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding new student in a database...")    # Will get called automatically

s1=Student("Harsh",90)
print(s1.name,s1.marks)

s2=Student("Luffy",80)
print(s2.name,s2.marks)


# Classes & Instacne Attributes

# Class.attr
# obj.attr
class Student():
    college_name="VJTI"  # Class Attribute
    name="Anonymous"     

    # Parameterized constructors
    def __init__(self,name,marks):
        self.name=name   # Object Attribute
        self.marks=marks
        
s1= Student("Zoro",20)
print(s1.name)          # Object Attribute
print(s1.college_name)  # Class Attribute
print(Student.name)     # Class Attribute

# Methods: Methods are functions that belong to objects

class Student():
    college_name="VJTI"  # Class Attribute

    # Parameterized constructors
    def __init__(self,name,marks):
        self.name=name   # Object Attribute
        self.marks=marks

    def welcome(self):
        print("Welcome Student",self.name)

    def get_marks(self):
        return self.marks
    
s1=Student("Zoro",20)
s1.welcome()
print(s1.get_marks())

# Create a StudentX class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class StudentX():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg(self):
        sum=0
        for val in self.marks:
            sum=sum+val
        print("Hi",self.name,"your avg score is",sum/3)
    
s1=StudentX("Sanji",[91,95,93])
s1.avg()
s1.name="Black Sanji"
s1.avg()

# Static Methods: Methods that don't use the self parameter(work at class level)
# class Student:
#    @staticmethod     # decorator
#    def college()
#        print("ABC College")
# Decorator allows us to wrap another function in order to extend the behaviour of the wrapped function, without modifying it

# 2 pillars of OOPS

# Abstraction: Hiding the implementation details of a class and only showing the essential features to the user

class Car:
    def __init__(self):
        self.acc= False
        self.brk= False
        self.clutch= False

    def start(self):
        self.clutch= True
        self.acc= True
        print("Car Started...")
c1=Car()
c1.start()

# Encapsulation: Wrapping Data and Functions into a single unit(object).

# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

class Account():
    def __init__(self,bal,accNo):
        self.bal=bal
        self.accNo=accNo

    def credit(self,cred):
        self.bal+=cred

    def debit(self,debt):
        self.bal-=debt

    def get_balance(self):
        print("Current Balance is: ",self.bal)

p1=Account(1000000,"TN123")
print(p1.bal)
print(p1.accNo)
p1.credit(250000)
p1.debit(500000)
p1.get_balance()
