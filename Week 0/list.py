# marks = [23, 45, 67, 89, 12]
# print(marks)  
# print(type(marks)) #list
# print(marks[0]) #first element
# print(len(marks)) #length of list

student = ["Shaurya", 23, 95.67, "Chandigarh"]
# print(student) #list

# student[0] = "Shivam" #changing the first element
# print(student) #list

#list slicing
""" print(student[0:2]) #first two elements
print(student[1:]) #all except first element
print(student[:2]) #first two elements
print(student[1:3]) #second and third elements
print(student[-1]) #last element
print(student[-2:]) #last two elements
print(student[-2:-1]) #second last element """

#list methods
""" student.append("Delhi") #adding element at the end
print(student) #list
student.insert(1, "Shivam") #adding element at index 1
print(student) #list
student.remove("Shivam") #removing element
print(student) #list
student.pop() #removing last element
print(student) #list
student.pop(1) #removing element at index 1
print(student) #list
student.reverse() #reversing the list
print(student) #list
student.clear() #clearing the list
print(student) #list """


#TUPLE
#Tuple is immutable
#Tuple is ordered
#Tuple is indexed
#Tuple is iterable

""" tuple = ("Shaurya", 23, 95.67, "Chandigarh")
print(tuple) #tuple
print(type(tuple)) #tuple
print(tuple[0]) #first element
print(len(tuple)) #length of tuple
tup = (1)
print(type(tup)) #int
tup = (1,) #single comma is important in case of single element tuple
print(type(tup)) #tuple """

#tuple slicing
""" print(tuple[0:2]) #first two elements
print(tuple[1:]) #all except first element
print(tuple[:2]) #first two elements
print(tuple[1:3]) #second and third elements
print(tuple[-1]) #last element
print(tuple[-2:]) #last two elements
print(tuple[-2:-1]) #second last element """


#tuple methods
tuple1 = (1, 2, 3, 4, 5)
print(tuple1.index(3)) #index of first occurrence of 3
print(tuple1.count(3)) #count of 3

