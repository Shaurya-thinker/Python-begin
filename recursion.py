# def show(n):
#     if(n == 0):
#         return

#     print(n)
#     show(n-1)    

# n = 10
# show(n)    

def fac(n):
    if(n == 0 or n == 1):
        return

    else:
        return n * fac(n-1)    

fac(5)        