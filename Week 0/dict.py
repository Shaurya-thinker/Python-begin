info = {
    "Key" : "value",
    "name" : "Shaurya",
    "learning" : "python",
    "age" : 19,
    "isStudent" : True,
    "subjects" : ["python", "java", "c++"],
    "marks" : [91, 92, 93,],
    12 : 90,
    (1, 2, 3) : "tuple",
}

print(info['name'][1])

""" print(info) #unordered
print(info["Key"]) #accessing value using key
print(type(info))
print(info["name"])
print(info[12])

info["name"] = "Shivam" #mutable
print(info["name"])
info["surname"] = "Shukla" #adding new key-value pair
print(info) """

# null_dict = {}
# print(null_dict) #empty dictionary
# print(type(null_dict)) #empty dictionary


#Nested Dictonary
""" Student = {
    "name" : "Shaurya",
    "score" : {
        "Chemistry" : 90,
        "Maths" : 95,
        "Physics" : 88
    }
}
print(Student)
print(Student["score"]["Maths"])

print(Student["score"]["Maths"] + Student["score"]["Chemistry"])

#dictorionary methods

print(list(Student.keys())) #returns all the keys not nested keys but only the first level keys
print(Student.values()) #returns all the values
print(Student.items()) #returns all the key-value pairs
print(Student.get("name"))
print(len(Student)) #returns the length of the dictionary
Student.update({"city" : "Chandigarh"}) #updates the value of the key
print(Student) """


#WAP To flowing meaning in python dictionary
""" my_dict = {
    "table" : ["a piece of furnitures", "list of facts & figures"],
    "cate" : "a small animal"
}
print(my_dict) """

#WAP to take input from the user and fill an empty dictionary
""" marks = {}

x = int(input("Enter phy: "))
marks.update({"phy" : x})

x = int(input("Enter chem: "))
marks.update({"chem" : x})

x = int(input("Enter maths: "))
marks.update({"maths" : x})

print(marks) """
