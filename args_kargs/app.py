def addition(*args):
    my_sum = 0
    print(args)
    print(type(args))
    for element in args:
        my_sum += element

    return my_sum

print(addition(10, 20, 30, 2.3, 4.5))
print(addition())

print()

def do_math(*args, **kwargs)
    if kwargs

