# num = input("Enter the number: ")
# i = 0  #Iterator 
# while(i <=4): #iteration
#     print("Hello" + name)
#     i += 1

# print(i)

#print numbers from 100 to 1
""" i = 100
while i >= 1:
    print(i)
    i -= 1 """


#print mutiplication of a number n
""" n = int(input("Enter the number: "))
i = 1
while i<=10:
    print(n, "*", i, "=", n*i)
    i += 1 """

# print elements of a list
""" list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i<len(list):
    print(list[i])
    i += 1 """    

#search for an element in a list
""" list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 36
i = 0
while i < len(list):
    if(list[i] == x):
        print("The index of the element is: ", i)
        break
    else: 
        print("Finding...")        
    i += 1     """



#FOR LOOP
#Loops are used for sequential traversal. For Traversing list, string, tuples etc.

#for a list
""" list = [1, 2, 4]
for num in list:
  print(num) """

#for a tuple
""" tuple = (1, 2, 3, 4, "Hello")
for st in tuple:
   print(st)  """   

#for a set
""" Set = {1, "Hello", "Hello", 1}
for el in Set:
   print(el) """

#For a dictionary
""" Dict = {
    "Veggies" : {
        "Potatoes" : 1,
        "Tomatoes" : 4,
        "Cucumber" : 5
    },
    "Name" : "Shaurya",
    "Class" : 2
}
for thih in Dict:
    print(thih)  #Only The Keys will get printed not the values """

#for String
""" str = "Shaurya Vrat"
for int in str:
    print(int)
else:
    print("End")     """

""" str = "Shaurya Vrat"

for char in str:
    if(char == 'a'):
        print("a found")
        break
    print(char)

else:
    print("END") """    


#RANGE FUNCTION

# print(range(5))

# el = range(5)
# print(el[0])
# print(el[1])

# el = range(3, 33, 3)
# for i in el:
#     print(i)

# for el in range(5):
#     print(el)    

# for el in range(1, 5):
#     print(el)    

# for el in range(3, 31, 3):
#     print(el)


############ pass Statement ##########    

for el in range(10):
    pass #empty, no work in the loop
