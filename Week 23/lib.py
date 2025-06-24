#import time
#time.time()
""" def usingWhile():
    i = 0
    while i<5000:
        i += 1
        print(i)

def usingFor():
    for i in range(5000):
        print(i)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(t1)
print(time.time() - init) """



#time.sleep()
""" print(4)
time.sleep(3)
print("This is printed after 3 sec") """


#time.strftime()
""" t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time) """



#datetime module
""" from datetime import datetime

now = datetime.now()
print("Date:", now.strftime("%D"))
print("Time:", now.strftime("%H:%M:%S")) """


#random module
""" import random

n = random.randint(2,8)
print(n)

n = random.randrange(2,8) # 8 not included
print(n)

list = [10, 20, 30, 50, 80]
print(random.choice(list))

print(random.uniform(3, 5))

random.shuffle(list)
print(list) """



#Random Password generate
import random
import string

def generate_random(length):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("Genrate password:", generate_random(12))



#Slot Booking 

import random 
import string
from datetime import datetime

def Slot_Booking(length):
    char = string.digits
    slot = ''.join(random.choice(char) for _ in range(length))
    return slot
now = datetime.now()    
print("Date:", now.strftime("%Y:%m:%d"))
print("Time:", now.strftime("%H:%M:%S"))
print("Alloted Slot:", Slot_Booking(5))