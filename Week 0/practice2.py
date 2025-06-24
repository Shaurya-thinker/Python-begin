""" with open("practice.txt", "a") as f:
    f.write("Hii everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.") """


## WAP to replace java with python in the file
""" with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)       

with open("practice.txt", "w") as f:
    f.write(new_data) """

""" def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
       data = f.read()
       if(word in data):
          print("Found")  
       else:
          print("not found")

def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
               print(line_no)
               return 
            line_no += 1     

    return -1

check_for_line()  """       


""" count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]
      
    nums = data.split(",")  
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count) """        
   



""" class Car:
    brand = "Lamborghini"
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print("The brand of car is: ", self.brand)
        print("The brand of car is: ", self.model)
        print("The brand of car is: ", self.year)

c1 = Car("Bugatti", "Vereon", 2005)
#c1.display()
print(c1.brand)
c1.brand = "Ford"
print(c1.brand) """

""" class Employee:
    Company_name = "Ficode software solution pvt Ltd"

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)

e1 = Employee("Shaurya", 1522)
print(e1.Company_name)
e1.display() """

""" class Animal:
    def __init__(self):
        pass

    @staticmethod
    def speak():
        pass

class dog(Animal):
    def __init__(self):
        pass

    @staticmethod
    def speak():
        print("bark")

d1 = dog()
d1.speak() """


""" class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


    def deposit(self, ammount):
        print("The deposited ammount is", ammount) 
        self.__balance = self.__balance + ammount
        print("Now the balance is:", self.__balance)

    def withdraw(self, ammount):
        print("The withdrawl ammount is", ammount)
        self.__balance = self.__balance - ammount 
        print("Now the remaning balacne is:", self.__balance)
        

b1 = BankAccount(250000)

b1.deposit(50000)
b1.withdraw(50000) """
     

""" class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("[name]:", self.name, "[age]:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print("[Employee_id]: ", self.employee_id)
    


class Manager(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display(self):
         print("[name]: ", self.name, "[age]: ", self.age, "[department]: ", self.department)


e1 = Employee("Rakesh", 32, "1634")
m1 = Manager("Vikas", 36, "Web development")

e1.display()
m1.display() """



""" class Cat:

    @staticmethod
    def make_sound():
        print("meow")

class Dog:

    @staticmethod
    def make_sound():
        print("Bark")


c1 = Cat()
d1 = Dog()

Animal = [c1, d1]

for animal in Animal:
    animal.make_sound() """


""" class Calculator:
    def add(self, *args):
        return sum(args)

c1 = Calculator()
print(c1.add(2, 4, 5, 11)) """



""" class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __len__(self):
        return len(self.title)

b1 = Book("Harry potter", "J.K Rowling")
b2 = Book("Harry potter", "J.K Rowling")
b3 = Book("Data Science", "Jane Doe")

print(str(b1))
print(b1 == b2)
print(b1 == b3)
print(len(b1)) """


""" class Mathops:
    name = "Shaurya"
    @staticmethod
    def is_even(a):
        if(a%2 == 0):
            print("even")
        else:
            print("odd")

    @classmethod
    def class_name(cls):
        print(cls.name)

m1 = Mathops()
m1.is_even(4)
m1.class_name() """

""" from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
    
class Rectangle(Shape):

    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def area(self):
        return self.length * self.breath
    
c1 = Circle(5)
r1 = Rectangle(20, 45)

print(c1.area())
print(r1.area()) """


""" class Vector:

    def __init__(self, real, image):
        self.real = real
        self.image = image

    def showNum(self):
        print(self.real, "i +", self.image, "j")
    

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.image + num2.image
        return Vector(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.image - num2.image
        return Vector(newReal, newImg)

    def __mul__(self, num2):
        newReal = self.real * num2.real
        newImg = self.image * num2.image
        return Vector(newReal, newImg)



v1 = Vector(4, 5)
v2 = Vector(3, 6)

v1.showNum()
v2.showNum()

v3 = v1 + v2
v3.showNum()

v3 = v1 - v2
v3.showNum()

v3 = v1 * v2
v3.showNum() """


""" class InvalidPasswordError(Exception):
    pass

class LoginSystem:
    def __init__(self):  
        self.passw = None

    def enter_pass(self):
        self.passw = input("Enter the password: ")
        if len(self.passw) < 8:
            raise InvalidPasswordError("Password must be at least 8 characters long.")
        
    def print_pass(self):
        print("Stored Password:", self.passw)


l1 = LoginSystem()

try:
    l1.enter_pass()
    l1.print_pass()
except InvalidPasswordError as e:
    print("Error:", e) """


""" class Engine:

    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP has started"
    
class Car:

    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def start_car(self):
        print(f"Car model {self.model}")
        print(self.engine.start())

engine = Engine(120)

c1 = Car("Toyota", engine)

c1.start_car() """


""" class Contacts:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Phone_Book:
    def __init__(self):
        self.contacts = []

    def add_contacts(self, contact):
        self.contacts.append(contact)

    def del__contacts(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]

    def search__contacts(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                return c
        return None
    
    def display_all(self):
        for c in self.contacts:
            print(f"{c.name} - {c.phone} - {c.email}")

c1 = Contacts("Shaurya", "shauryavratshukla@gmail.com", 8604127482)
p1 = Phone_Book()
c2 = Contacts("Yash", "yashvratshukla@gmail.com", 9415127482)
p1.add_contacts(c1)
p1.add_contacts(c2)
p1.display_all() """


""" class Book:  # Class names should be capitalized by convention
    def __init__(self, title, author, year):
        self.title = title
        self.author = author 
        self.year = year


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):  # Better name: 'add_book' (not 'add__books')
        self.books.append(book)

    def del_book(self, title):  # Fix: logic and spelling
        self.books = [b for b in self.books if b.title != title]

    def display_all_books(self):
        for b in self.books:
            print("Title:", b.title, "Author:", b.author, "Year:", b.year)



b1 = Book("The Great Gatsby", 'F. Scott Fitzgerald', 1925)
b2 = Book("1984", "George Orwell", 1949)


l1 = Library()

l1.add_book(b1)
l1.add_book(b2)

print("Before deleting:")
l1.display_all_books()

l1.del_book("1984")

print("\nAfter deleting:")
l1.display_all_books() """

""" import json
import csv

list = ['Shaurya', 'akansh', 'panshul', 'ananya', 'harsh']

with open("name.txt", 'w') as file:
    file.write(str(list))
    
with open("name.txt", 'r') as file:
    data = file.read()
    print(data)

with open("name.json", 'w') as file:
    json.dump(list, file)

with open("name.json", 'r') as file:
    data = json.load(file)
    print(data)


with open("name.csv", 'w', newline= '') as file:
    writer = csv.writer(file)
    for name in list:
        writer.writerow([name]) """


