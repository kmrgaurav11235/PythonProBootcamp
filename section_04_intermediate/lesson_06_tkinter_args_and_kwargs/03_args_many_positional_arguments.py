# Unlimited number of arguments for a function / method
def add(*args):
    # The name "args" is convention. You can use any other name too, the important part is the '*'
    # print(type(args))  # 'args' will be in form of a tuple
    # print(args)
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum


print(add(1, 2, 3, 4))
print(add(1, 2, 3))
print(add(1))
print(add(1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1))
print(add())
