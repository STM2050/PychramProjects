def greet():
    print("Hi")
    print("Hello!")
    print("Greeting!")

greet()
greet()
greet()

print()

def some_func(x, y):
    value = x + y
    return value

print(some_func(5, 4.5))

a = some_func(2, 2.5)
print(a)

print(some_func(some_func(2, 2), some_func(3.5, 4.34)))

print()

def some_func2(x, y):
    return x * y
print(some_func2(2, 3))

print()
b = 10
def some_func3():
    b = 20
    print(b)

print()
def some_func4():
    print(b)
print(b)
some_func3()

some_func4()