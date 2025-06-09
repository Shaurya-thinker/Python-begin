# print((lambda x, y: x + y)(5, 6))   # can have only single-line expression

def my_map(my_func, my_itr):
    result = []
    for item in my_itr:
        new_item = my_func(item)
        result.append(new_item)
    return(result)
nums = [3, 4, 7, 8]

cubed = my_map(lambda x: x**3, nums)

print(cubed)

