print("Hello World")

# Declare Variables
myNumber = 3
print(myNumber)

myNumber2 = 4.5
print(myNumber2)

myNumber = "helloworld"
print(myNumber)

print()

# Empty List
nums = []

# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")

print(nums)

dict = []

dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

print(dict)

my_dict_1 = []

my_dict_1 = {'first_name': 'Shaquera', 'last_name':'Moore', 'age': '30'}

print(my_dict_1)

print()

print(my_dict_1.get('last_name'))

print()

tup = ('Geeks', 'For', 'Geeks')

print(tup)

print()
print(tup.count('Geeks'))
print(f"tup has {tup.count('Geeks')} Geeks")

print()


set = set(["Shaquera", "T", "Cavill"])

print(set)
set.add("Henry")
print(set.pop())
print(set)
set_1 = {"Shaquera", "Jimin", "T"}

print()
print(set.intersection(set_1))
print(set.union(set_1))
print(set.difference(set_1))

name = input("Enter your Name")
password = input("Enter password")

print()
print("Hello", name, password)

print()

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

num3= num1 // num2
print("Quontient is:", num3)

print()
num_1 = 34
if(num_1>12):
    print("Num_1 is good")
elif(num_1>35):
    print("Num_2 is not goooo.....")
else:
    print("Num_2 is great")


