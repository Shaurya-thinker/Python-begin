# String
#Esccape sequences characters
""" str1 = "This is a string.\nWe can use it to store text."
print(str1)

str1 = "This is a string.\tWe can use it to store text."
print(str1) """

#basic string operations
# string concatenation and repetition
""" str1 = input()
str2 = input()

print(str1 + " " +  str2)
print(str1*2) """

#length of string
""" str1 = "This is a string."
len1 = len(str1)
print("Length of string is: ", len1) """

#indexing and slicing
""" str = "Shaurya Vrat"
#str[3] = "s" changes are not allowed 
print(str[3])

print(str[1 : 4])
print(str[ : 4]) #[0:4]
print(str[1 : ]) #[1:len(str)]
print(str[ : ]) #[0:len(str)]
print()
print(str[-1]) #last character
print(str[-3 : -1]) #-1 is not included 
print(str[-3 : ]) #last 3 characters
print(str[ : -1]) #all except last character
print(str[-1 : -4]) #empty string """

str = "shaurya Vrat"
str = str.replace("a", "o") #replaces all occurrences of "a" with "o"
print(str)

str = str.capitalize() #capitalizes first character
print(str)

print(str.endswith("t")) #checks if string ends with "t"
print(str.startswith("S")) #checks if string starts with "S"

print(str.find("o")) #returns the index of first occurrence of "o"
print(str.find("ot")) #returns the index of first occurrence of "ot"

print(str.count("a")) #counts the number of occurrences of "a"
print(str.count("o"))