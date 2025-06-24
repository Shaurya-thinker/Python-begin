# try:
#     number = int(input("Enter a number"))
#     if(number == 0):
#         print("Enter the valid number")
#     if(type(number) == <class 'str'>)
#     print(1/number)

# except ZeroDivisionError:
#     print("You can't divide by zero NOOB!!")
# except ValueError:
#     print("Enter only numbers please")
# except Exception:
#     print("Something went wrong!")

# finally:
#     print("Do some clean up")


number = [23, 43, 43, 23, 54]
name = "shaurya"

print(type(number))
print(type(name))

print(type(number) == type(name))
print(isinstance(number, (int, str, list)))