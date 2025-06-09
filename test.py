""" with open("hello.txt", "a") as file:
    data = file.write("\nHello python") """


## Count the number of lines
""" with open("hello.txt", "r") as file:
    line_no = 0
    for line in file:
        print(line.split())
        line_no += 1

print(line_no) """

## replace the occurence
""" with open("hello.txt", "r") as file:
    data = file.read()
    
new_data = data.replace("python", "java")
print(new_data)

with open("hello.txt", "w") as file:
    file.write(new_data) """


""" num = 2  # The line number you want to print

with open("hello.txt", "r") as file:
    for current_line_no, line in enumerate(file, start=1):
        if current_line_no == num:
            print(f"Line {num}:", line.strip())
            break """


""" import json

employee = {
    "name" : "Shaurya",
    "age" : 19,
    "job" : "intern software engineer"
}

file_path = "C:/Users/Dhruva/OneDrive/Desktop/hello.json"

with open(file_path, "a") as file:
    json.dump(employee, file, indent= 4)

with open(file_path, "r") as file:
    data = file.read()
    print(data) """







    