""" class Students:
    name = "Shaurya"

s1 = Students()
print(s1.name)    """ 


""" class car:
    colour = "Blue"
    brand = "BMW"

car1 = car()
print(car.colour)    
print(car.brand) """

#CONSTRUCTOR / init function

""" class Student:
    name = "Shaurya"

    #default constructor
    def __init__(self):
        pass

    #prameterized constructor
    def __init__(self, name, marks):
        #print(self) #points ar the object
        self.name = name
        self.marks = marks
        #print("adding new student in database..")

s1 = Student("Shaurya", 95)
#print(s1)  #self
print(s1.name, end= " ")
print(s1.marks)

s2 = Student("Akanshhh", 97)
print(s2.name, end=" ")
print(s2.marks) """


""" class Student:
    college_name = "CU" #Class attribute
    name = "Anonymous" # obj.attr has greater precedence than class.attr
    def __init__(self, name, marks):
        self.name = name  # instance attribute
        self.marks = marks
        #rint("adding new student in database..")

s1 = Student("Shaurya", 95)
print(s1.name, s1.marks)

s2 = Student("Akanshhh", 97)
print(s2.name, s2.marks)

print(Student.college_name)
print(s1.college_name)
print(s2.college_name) """

##  Methods
""" class Student:
    college_name = "CU"

    def __init__(self, name, marks):
        self.name = name  
        self.marks = marks

    def welcome(self):
        print("Welcome Student,", self.name)   

    def get_marks(self):
        return (self.marks)     

s1 = Student("Shaurya", 95)
s1.welcome()
print(s1.get_marks()) """


##########   STATIC METHOD
""" class Student:
    college_name = "CU"

    def __init__(self, name, marks):
        self.name = name  
        self.marks = marks

    @staticmethod    
    def hello():
        print("hello")

    def welcome(self):
        print("Welcome Student,", self.name)   

    def get_marks(self):
        return (self.marks)     

s1 = Student("Shaurya", 95)
s1.welcome()
print(s1.get_marks())
s1.hello() """


######## ABSTRACTION

""" class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car Started...") 

car1 = Car()
car1.start() """


### del Keyword
""" class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Shaurya")
print(s1.name)
del s1.name
print(s1.name) """


# private

""" class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
            print(self.__acc_pass)

acc1 = Account("122342", "sfs2sd")

print(acc1.acc_no)
acc1.reset_pass() """

