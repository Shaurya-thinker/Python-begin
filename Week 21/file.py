##########READ FILE
""" f = open("demo.txt", "r")

data = f.read()
print(data)
print(type(data))

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close() """



###########WRITE IN FILE
#write with character "w" will overwrite the original file
""" f = open("demo.txt", "w")
f.write("This is new line")
f.close() """


#write with character "a" will add a new line and the original text will remain unchanged
""" f = open("demo.txt", "a")
f.write("\nThis is the second line")
f.close() """
 

""" f = open("sample.txt", "w") # if the file doesn't exist and we are using write characters then the compiler will make the file for us  
f.write("Hello this is Shaurya")
f.close() """


####################### It overwrites that much character which it has in it
""" f = open("demo.txt", "r+")
f.write("abc")
print(f.read())
f.close() """


""" f = open("demo.txt", "w+")
f.write("abc")
print(f.read())
f.close() """


####### with syntax

""" with open("demo.txt", "r") as f:
    print(f.read())


with open("demo.txt", "w") as f:
    f.write("new data") """    

########## REMOVE
""" import os

os.remove("demo.txt") """





### Python writing files (.txt, .json, .csv)
#### .txt 
## "w" mode
""" txt_data = "I like pizza!"

file_path = "C:\\Users\\Dhruva\\OneDrive\\Desktop\\output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was creatd") """


## "x" mode
""" txt_data = "I like pizza!"

file_path = "C:\\Users\\Dhruva\\OneDrive\\Desktop\\output.txt"

try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was creatd")
except FileExistsError:
    print("That file already exists!") """

## "a" mode
""" txt_data = "I like pizza!"

file_path = "C:\\Users\\Dhruva\\OneDrive\\Desktop\\output.txt"

try:
    with open(file_path, "a") as file:
        file.write("\n" + txt_data)
        print(f"txt file '{file_path}' was creatd")
except FileExistsError:
    print("That file already exists!") """


## collections

""" employees = ["Eugene","Squidward", "Spongebob", "Patrick"]

file_path = "C:\\Users\\Dhruva\\OneDrive\\Desktop\\output.txt"

try:
    with open(file_path, "a") as file:
        #file.write(str(employees))
        for employee in employees:
            file.write(employee +"\n")
        print(f"txt file '{file_path}' was creatd")
except FileExistsError:
    print("That file already exists!") """




######## JSON files 
""" import json


employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "C:\\Users\\Dhruva\\OneDrive\\Desktop\\output.json"

try:
    with open(file_path, "a") as file:
        json.dump(employee, file, indent=4)  # will turn the dictionary into json string
        print(f"json file '{file_path}' was creatd")
except FileExistsError:
    print("That file already exists!") """


#### CSV files

""" import json
import csv
employee = [["Name", "Age", "Job"], 
            ["Spongebob", 30, "Cook"], 
            ["Patrick", 37, "Unemployed"], 
            ["Sandy", 27, "Scientist"]]

file_path = "C:\\Users\\Dhruva\\OneDrive\\Desktop\\output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print(f"csv file '{file_path}' was creatd")
except FileExistsError:
    print("That file already exists!") """




######## python reading files(.txt, .json, .csv)

""" file_path = "C:/Users/Dhruva/OneDrive/Desktop/output.txt"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found") """

##Not having permit to read the file
""" file_path = "C:/Users/Dhruva/OneDrive/Desktop/output.txt"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have access to read that file") """


## reading json file
""" import json

file_path = "C:/Users/Dhruva/OneDrive/Desktop/output.json"

try:
    with open(file_path, 'r') as file:
        content = json.load(file)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have access to read that file") """

## reading a csv file
""" import csv

file_path = "C:/Users/Dhruva/OneDrive/Desktop/output.csv"

try:
    with open(file_path, 'r') as file:
        content = csv.reader(file)
        for line in content:
            print(line[1])
except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have access to read that file") """