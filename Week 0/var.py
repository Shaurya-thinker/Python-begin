""" print ("My name is var.py", "My age is 12.")
print (23 + 45) 
name = "Shaurya"
age = 14
print ("My name is: ", name)
print(type(name)) # This will print the data type of variable name
print(type(age)) # This will print the data type of variable age
print (name + " is " + str(age) + " years old.") # This will print the name and age
age2 = 15
old = False
a = None
print(type(old)) # This will print the data type of variable old
print(type(a)) # This will print the data type of variable a
sum = age + age2
print (sum) # This will print the sum of age and age2




A, B = 2, 3
Txt = "@"
print(A*Txt*B) # This will give the output as the string @ repeated 6 times

A, B = "2", 3
Txt = "@"
print((A+Txt)*B) # This will first concatenate the string "2" and "@" and then repeat it 3 times """


#INPUT IN PYTHON 


name = input("name : ")
age = int(input("age : "))
price = float(input("price : "))

print("My name is", name, "and my age is", age, "and my price is", price)




number = [23, 43, 43, 23, 54]
name = "shaurya"

print(type(number))
print(type(name))

print(type(number) == type(name))
print(isinstance(number, (int, str, list)))