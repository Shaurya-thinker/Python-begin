age = int(input("Age: "))
if(age >= 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")   

# The above code checks if a person is eligible to vote based on their age.

food = input("Enter your favorite food: ")
eat = "yes" if food.lower() == "cake" else "no"
print(eat)
# The above code checks if the user's favorite food is cake and assigns "yes" or "no" to the variable eat.

print("You can eat cake") if food.lower() == "cake" else print("You cannot eat cake")

age = int(input("Enter your age: "))
vote = ("yes", "no") [age < 18]
print(vote)
