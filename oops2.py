#Single level inheritance
""" class Car:
    colour = "Black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped..")    

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

car1.start()

print(car1.name)
print(car1.colour) """


## multi-level inheritance
""" class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped..")    

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

f1 = Fortuner("diesel") 
f1.start() """        



## Multiple inheritance
""" class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)  
print(c1.varB)
print(c1.varA) """


### Super method
""" class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped..")    

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.type) """      


## Class Method
""" class person:
    name = "Anonymous"

    def changeName(self, name):
        self.name = name
        person.name = name
        self.__class__.name = name

    @classmethod     #attributes will change directly in the class
    def changeName(cls, name):
        cls.name = name    

p1 = person()        
p1.changeName("Shaurya Vrat Shukla")
print(p1.name)
print(person.name) """


## property decorator

""" class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.math + self.phy + self.chem)/3) + "%"

stu1 = Student(98, 97, 99)   
print(stu1.percentage) 

stu1.phy = 86
print(stu1.percentage) """


## Polymorphism

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")    

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img    
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)    

num1 = Complex(1, 3)
num1.showNumber()     

num2 = Complex(4, 7)
num2.showNumber()


#num3 = num1.add(num2)
num3 = num1 + num2
num3.showNumber()


num3 = num2 - num1
num3.showNumber()