""" collection = {1, 2, 3, 4, "Hello", "Hello", "World", 4}

print(collection)
print(type(collection))
print(len(collection))


# collection = {} # empty dictionary

collection2 = set() # empty set
print(type(collection2))


# Set Methods
collection.add("Shaurya")
print(collection)

collection.remove(1)
print(collection)

collection.pop()
collection.pop()
print(collection)

# collection.clear()
# print(collection)

collection3 = {4, 2, 1, "Hello", "Spidey"}

print(collection.union(collection3))
print(collection.intersection(collection3)) """


""" Classroom = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(Classroom)
print(len(Classroom))
print(type(Classroom)) """

# WAP so that 9 and 9.0 will store as a seprate value in a set
Set = {("int", 9), ("float", 9.0), "Help", 9, 1, 4}
print(Set)