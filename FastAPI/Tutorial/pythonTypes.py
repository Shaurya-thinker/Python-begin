def add(firstname: str, lastname: str): #pre-defined the type of the variable
    if(firstname != None):
     firstname.capitalize()

     
    return firstname + " " + lastname


fname = "John"
lname = "Walker"

name = add(fname, lname)
print(name)