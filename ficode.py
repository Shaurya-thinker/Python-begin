Movies = {
    "Genre" : {
        "action" : ["Peaky blinders", "Breaking bad", "John Wick"],
        "comedy" : ["Hangover", "phir hera pheri", "Dhammal"],
        "fantasy" : ["Harry potter", "Lord of the rings", "Game of thrones"],
        "romantic" : ["La la Land", "Spder man", "My fault"]
    }
}
print("Choose a movie genre: ")
print("1. action")
print("2. comedy")
print("3. fantasy")
print("4. romantic")
mov = input()
if(mov.lower() == "action"):
    print(Movies["Genre"]["action"])
elif(mov.lower() == "comedy"):
    print(Movies["Gnere"]["comedy"])
elif(mov.lower() == "fantasy"):
    print(Movies["Genre"]["fantasy"])
elif(mov.lower() == "romantic"):
    print(Movies["Genre"]["romantic"])
else: 
    print("Invalid input")

print("Do you want to suggest movie in your genre: yes or no")
choice = input()

if choice.lower() == "yes":
    print("Enter the movie name for " + mov + " genre")
    sugg = input()
    new_dict = {
        mov : sugg
    }
    Movies.update(new_dict)
else:   
    print("NULL") 

print(Movies)    



