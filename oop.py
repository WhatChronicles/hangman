# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old"
    
    #Creating instances of the person class
# person1= person("Alice",30)
# person2=person("Bobb",25)

#Accessing instances variables and calling methodes
# print(person1.name)
# print(person2.age)

# message = person1.greet()
# print(message)  


#Single level inheritance

# class Animal:
#     def speak(self):
#         return "\nAnimal speaks"
# class dog(Animal):
#     def bark(self):
#         return "\nDog Barks" 
    #Dog inherits from Animal
# my_dog = dog()
# print(my_dog.speak())
# print(my_dog.bark())

 #Multiple inheritance

# class A:
#     def method_A(self):
#         return "\nMethod A"
    
# class B:
#     def method_B(self):
#         return "\nMethod B"
    
# class C(A,B):
#     def method_C(self):
#         return "\nMethod C"
    
#C inherits form both a and b
# obj_c=C()
# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_C())

 #Multilevel inheritance

# class A:
#     def method_A(self):
#         return "\nMethod A"
    
# class B(A):
#     def method_B(self):
#         return "\nMethod B"
    
# class C(B):
#     def method_C(self):
#         return "\nMethod C"
    
#C inherits from B which inherits from A

# obj_c=C()
# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_C())


# SUPER()
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
# class Square(Rectangle):
#     def __init__(self, side_length):
#         super().__init__(side_length, side_length)  # Call the parent class constructor

#Creating instances of square and recgtangle
# Rectangle1 = Rectangle(5, 10)
# Square1 = Square(4)
# print("Area of Rectangle:", Rectangle1.area())
# print("Area of Square:", Square1.area())

#encapsulation
# class MyClass:
#     def __init__(self):
#         self.__private_variable="private"
#     def get_private_variable(self):
#         return"This is a private variable"

# obj =MyClass()
# print(obj.get_private_variable())


#protected method
# class Base:
#     def __init__(self):
#         self._protected_variable = "This is a protected variable"
# class Derived(Base):
#     def access_protected_variable(self):
#         return self._protected_variable 
# print("Accessing protected variable:", Derived().access_protected_variable())

#Polymorphism
#Operator Overloading
#Method overwriting
#Duck Typing



#Introduction to Exceptions

#Raise inbuilt exceptions to handle different cases with different except block

# try:
#     x= int(input("Enter a number: "))
#     y= int(input("Enter another number: "))
#     result = x / y
#     print(f"The result of {x}/{y} is {result}")

# except ZeroDivisionError as e:
#     print("Error: Division by zero is not allowed.", e)
#     print("Please enter a non-zero number for the second input." )
#     x= int(input("Enter a non-zero number: "))
#     y= int(input("Enter another number: "))  
#     result = x / y
#     print(f"The result of {x} divided by {y} is {result}")

# except TypeError as e:
#     print(e)  
#     print("Error: Invalid input type. Please enter numeric values.")
#     x = int(input("Enter a number: "))
#     y = int(input("Enter another number: "))
#     result = x / y
#     print(f"The result of {x} divided by {y} is {result}")


# except Exception as e:
#     print(e)  
#     print("Error: Invalid input type. Please enter numeric values.")
#     x = int(input("Enter a number: "))
#     y = int(input("Enter another number: "))
#     result = x / y
#     print(f"The result of {x} divided by {y} is {result}")



# def add():
#     try:
#         x=int(input("\nEnter a number:"))
#         y=int(input("\nEnter second number:"))
#         result=x/y
#         print("result",result)

#     except Exception as e:
#         print(e)
#         print("Enter a correct value")
#         add()

# add()

#Raise Custom Exception to handle different cases with same Except block

# x = int(input("\n---Enter your age---:"))

# try:

#     if x>120:
#         raise Exception("Sorry,You cannot be above 120 years old")
    
#     elif x== 0:
#         raise Exception("Sorry,your age cannot be zero")
#     print(f"My age is {x}")

# except Exception as e:
#     print(e)
#     x=int(input("Re-Enter your age:"))
#     print(f"My age is {x}")


#Created custom Exception to handle different cases

class negative_error(Exception):
    def __init__(self, message):
        super().__init__(message)

class zero_error(Exception):
    def __init__(self, message):
        super().__init__(message)

x= int(input("\n---Enter your age---:"))
try:
    if x < 0:
        raise negative_error("Sorry, your age cannot be negative")
    elif x == 0:
        raise zero_error("Sorry, your age cannot be zero")
    print(f"My age is {x}")

except negative_error as ne:
    print(ne)
    x = int(input("Re-Enter your age:"))
    print(f"My age is {x}")

except zero_error as ze:
    print(ze)
    x = int(input("Re-Enter your age:"))
    print(f"My age is {x}")