""" print("Enter the first number:")
a = int(input())
print("Enter the second number:")
b = int(input())
print("The sum of the two number is: ", a+b) """

#WAP for area of square
""" side = int(input("Enter the value of side: "))
print("The area of the suare is:", side*side) """

""" first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
print("The average of the two number is: ", (first+second)/2) """


""" a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# if a >= b:
#     print("True")
# else: 
#     print("False")    
print(a >= b) """

#String Questions

# Name = input("Enter the name: ")
# print(Name)
# print(len(Name))

# str = input("Enter the string: ")
# print(str)
# print(str.count("$"))


# Conditionals statements

""" print("Enter the marks of the student: ")
marks = int(input())
if marks >= 90:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >=70 and marks < 80:
    print("Grade C")
elif marks <70:
    print("Grade D")
else:
    print("Grade F")   """  


""" n = int(input("Enter the number: "))
if n%2 == 0:
    print("Even")
else: 
    print("Odd")     """


""" movie = []
mov1 = input("Enter the name of the movie: ")
mov2 = input("Enter the name of the movie: ")
mov3 = input("Enter the name of the movie: ")

movie.append(mov1)
movie.append(mov2)
movie.append(mov3)

print(movie) """

# WAP to check a list contains a palindrome of elements
""" list = [1, "abc", 3, "abc", 1]
list1 = list.copy() #return a shallow copy of the list

list1.reverse()
if list == list1:
    print("Palindrome")
else:
    print("Not a palindrome")    """ 


#WAP to print elements of a list using loop:

""" list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter the number to be searched: "))
idx = 0
for ins in list:
    if(ins == x):
        print(ins)
        print("Found the element at position: ", idx)
        break
    else:
        print(ins)
        idx += 1
else:
    print("Invalid")        

print("END")  """   

#WAP to print numbers from 1 to 100 and also 100 to 1

""" el = range(100)

for i in el:
    print(i) """

""" el = range(100, 0, -1) 

for i in el:
    print(i) """


#WAP the multiplication of number n

""" x = int(input("Enter the number: "))
el = range(x, x*11, x)

for i in el:
    print(i)

##OR

for i in range(1, 11):
    print(x * i) """


#WAP using while loop to find sum of first n numbers

""" x = int(input("Enter the number till which sum should continue: "))
i = 1
sum = 0
while(i <= x):
    sum += i
    i += 1

print(sum) """

#WAP to find factorila of first n numbers uisng for

""" x = int(input("Enter the number: "))
fac = 1

#While loop
"""# i = 1
#while i<= x:
#    fac *= i
#   i += 1

#print("Factorial:", fac)    """ 

#for loop
#for i in range(1, x+1):
#    fac *= i

#print(fac) """



####FUNCTIONS

#WAP to print the lenght of a list 

""" def cal_len(a):
    print(len(a))

list = [1, 32, 54, 21, 33]
cal_len(list)  """   


#WAP to print elements of the list in single line

""" def print_list(a):
    print(a)

list = [21, 42, 14, 15, 65]
print_list(list)   """  

#WAP to find the factorial of n

""" def cal_fac(n):
    fac = 1
    for el in range(1, n+1):
        fac *= el
    print(fac)

n = 5
cal_fac(5) """


#WAP to convert USD to INR

""" def inr_usd(a):
    print("The amount in INR is:", a*85.59)


x = int(input("Enter the amount in USD:"))
inr_usd(x) """    


######### WAP to create a student class that takes name & marks of 3 subjects as arguments in constructor
# Tehn create a method to print avg

""" class Subject:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def prin_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Subject("Tony Stark", [99, 98, 97])
s1.prin_avg() """



""" class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calArea(self):
        return 3.14*self.radius**2

    def calPara(self):
        return 2*3.14*self.radius


c1 = Circle(21)
print(c1.calArea())
print(c1.calPara()) """



""" class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(self.role)
        print(self.department)
        print(self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 50000)

e1 = Engineer("Shaurya", 19)
e1.showDetails() """



""" class Order:
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices

    def __gt__(self, order2):
        if(self.prices > order2.prices):
            print(True)
        else:
            print(False)


order1 = Order("Chicken", 200)
order2 = Order("Goat", 100)

order1 > order2 """

