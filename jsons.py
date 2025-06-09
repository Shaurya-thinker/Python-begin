import json

Student = [
    {
        "name": "Shaurya",
        "UID": "24BCS10586",
        "Batch": "BE-CSE",
        "Class": 608
    },
    {
        "name": "Panshul",
        "UID": "24BCS10792",
        "Batch": "BE-CSE",
        "Class": 611
    }
]

""" with open("file.json", 'w') as f:
    data = json.dump(Student, f, indent=2)
    print(data) """

""" with open("file.json", 'r') as f:
    data = json.load(f)


new_Student = {
    "name" : "Krish",
    "UID" : "24BCS11132",
    "Batch" : "BE-CSE",
    "Class" : 615
}

data.append(new_Student)

with open("file.json", 'w') as f:
    json.dump(data, f, indent=2)

print("Updated file is: ")
print(data) """




""" with open("bbok.json", 'r') as f:
    books = json.load(f)
    
    for book in books:
        title = book.get("Title", "Unknown title")
        Author = book.get("Author", "Unknown author")
        Year = book.get("Year", "Unknown year")

        print(f"Title: {title}")
        print(f"Author: {Author}")
        print(f"Year: {Year}")
        print("-" * 20) """


""" Friends = [
    {
        "Name" : "Shaurya",
        "Phone" : 9913232343
    },
    {
        "Name" : "Panshul",
        "Phone" : 9613532346
    },
    {
        "Name" : "Sarvesh",
        "Phone" : 9513236343
    },
    {
        "Name" : "Krish",
        "Phone" : 9813232357
    },
    {
        "Name" : "Sanidhya",
        "Phone" : 9413232348
    },
]

with open("Friends.json", 'w') as file:
    json.dump(Friends, file, indent=2)


with open("Friends.json", 'r') as f:
    friend = json.load(f)

    for dost in friend:
        Name = dost.get("Name", "Unknown Name")
        Phone = dost.get("Phone", "Unknown Phone")

        print(f"Name: {Name}")
        print(f"Phone: {Phone}")
        print("-" * 10)


with open("Friends.json", 'r') as file:
    data = json.load(file)


new_friend = {
        "Name" : "Ananya",
        "Phone" : 9425257257
}


data.append(new_friend)

print(data)

with open("Friends.json", 'w') as friend:
    json.dump(data, friend, indent=2) """ 
    



import csv
import json

########## CONVERT FROM CSV TO JSON
with open("name.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    Contacts = list(csv_reader)

with open("ontacts.json", 'w') as json_file:
    json.dump(Contacts, json_file, indent= 4)



############# CONVERT FROM JSON TO CSV
""" with open("ontacts.json", 'r') as json_file:
    contacts = json.load(json_file)

with open("ontacts_new.csv", 'w', newline= '') as csv_file:
    fieldnames = contacts[0].keys()
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(contacts) """


import json

def pretty_print_json_file(filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
            print(data)
            print(type(data))
            
pretty_print_json_file("ontacts.json")



""" with open("name.txt", 'r') as f:
    data = f.read()
    print(data)
    print(type(data)) """