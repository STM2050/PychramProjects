num = 1
while num <= 100:
    print(num, end=" ")
    num = num + 1

print()

print(type(range(1, 101)))

print()
for num in range(1,101):
    print(num, end=" ")

print()
for num in range(0, 100, 3):
    print(num, end=" ")

print()
for num in range(10):
    print(num, end=" ")

print()
for _ in range(1000):
    print("Hello")
for num in range(10, 0, -1):
    print(num)

print()
for char in "hello":
    print(char)

print()
while True:
    print("Welcome to the calculator app")
    num1 = int(input("Enter the first number you would like to add:"))
    num2 = int(input("Enter the second number you would like to add:"))

    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")

    should_contiune = input("Would you like to contiue? (Y/N):")
    if should_contiune.upper() == 'N':
        break