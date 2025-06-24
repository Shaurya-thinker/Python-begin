""" class phone_book:
    def __init__(self):
        pass


    def dict_cont(self):
        return  {
            "name" : self.name,
            "phone" : self.phone,
            "email" : self.email,
            "address" : self.address

        }

    def add_cont(self):
       self.name = input("Enter the name: ")
       self.phone = input("Enter the phone number: ")
       self.email = input("Enter the email: ")
       self.address = input("Enter the address: ")



C1 = phone_book()   
C1.add_cont()   
print(C1.dict_cont()) """ 




