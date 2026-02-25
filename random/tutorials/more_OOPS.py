# OOPS Part 2
# del keyword
# Used to delete object properties or object itself
# del s1.name
# del s1

# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("Harsh")
# print(s1.name)
# del s1.name
# print(s1.name)

# Private(like) attributes & methods
# Conceptual Implentation in Python
# Private attributes & methods are meant to be used only within the class and are 
# not accessible from outside the class.

class Account:
    def __init__(self,accNo,accPass):
        self.accNo=accNo
        self.__accPass=accPass    # Using 2 underscore(__) before any variable name can make them private

    def resetPass(self):
        print(self.__accPass)

acc1=Account("12345","TN123")

print(acc1.accNo)
# print(acc1.__accPass) Will give error because private modifier
print(acc1.resetPass()) # Will give value because called from class

# Inheritance: When one class(child/derived) derives the properties & methods of another class(parent/base).
# class Car:
#    ...
# class ToyotaCar(Car):
#    ...

class Car:
    color="Black"
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("Fortune")

print(car1.color)
print(car1.start())

# Types of Inheritance
# 1. Single Inheritance       Parent->Child
# 2. Multi-level Inheritance  Parent->Child->Child->...
# 3. Multiple Inheirtance     Parent1->Child<-Parent2

# super method
# super() method is used to access methods of the parent class

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

car1=ToyotaCar("Prius","Electric")
print(car1.type)

# class method
# A class method is bound to the class & recives the class as an implicit first argument.
# Note - static methods can't access or modify class state & generally used for utility.
# class Student:
#    @classmethod   decorator
#    def college(cls):
#         pass

class Person:
    name="Anonyomous"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
print(p1.changeName("Harsh"))
print(p1.name)
print(Person.name)

# Different methods till now:
# 1. Static Methods     No attributes 
# 2. Class Methods      (cls)  Class attribute
# 3. Instance Methods   (self) Object attributes


# Property: We use @property decorator on any method in the class to use the method as property
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
    
stu1=Student(98,97,99)
print(stu1.percentage)
stu1.phy=86
print(stu1.phy)
print(stu1.percentage)  # Giving same percentage as before

# Polymorphism: Operator Overloading
# When the same opertor is allowed to have different meaning according to the content
# Operator & Dunder functions
# a+b  addition         a.__add__(b)
# a-b  subtraction      a.__sub__(b)
# a*b  multiplication   a.__mul____(b)
# a/b  division         a.__truediv____(b)
# a%b  addition         a.__mod____(b)

print(1+2)
print(type(1))
print("Harsh"+"Sankhe") # Concatenation
print([1,2,3]+[4,5,6])  # Merge
# Here differnt meaning for addition hence we can say it is operator overloading

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumbers(self):
        print(self.real,"i +",self.img,"j")

    def add(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
    # With dunder functions
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)


num1=Complex(1,3)
num1.showNumbers()

num2=Complex(4,6)
num2.showNumbers()

num3=num1.add(num2)
num3.showNumbers()

num4=num3+num2
num4.showNumbers()

# Define a Circle class to create a circle with radius r using the constructor
# Define an Area() method of the class which calculate the area of the circle
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        self.ar=3.14*self.radius*self.radius
        print(self.ar)

    def perimeter(self):
        self.peri=2*3.14*self.radius
        print(self.peri)

c1=Circle(5)
c1.area()
c1.perimeter()

# Create a class called Order which stores item & its price
# Use dunder funtion __gt__() to convey that:
#     order1>order2 if price of order1>price of order2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price>odr2.price
    
odr1=Order("chips",20)
odr2=Order("tea",15)

print(odr1>odr2) # True
