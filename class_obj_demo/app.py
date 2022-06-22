class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hi(self):
        print(f"Hi, my name is {self.first_name} {self.last_name}, and I am {self.age}")

    def have_birthday_party(self):
        print("Hooray my birthday is today")
        self.age +=1
p1 = Person("John", "Doe", 30)
p2 = Person("Jane", "Doe", 25)
p3 = Person("Shaquera", "Moore", 32)

print(type(p1))
print(type(p2))
print(type(p3))

print(p1.first_name)
print(p2.first_name)
print(p3.first_name)

print(p1.last_name)
print(p2.last_name)
print(p3.last_name)

print(p1.age)
print(p2.age)
print(p3.age)

p1.say_hi()
p2.say_hi()
p3.say_hi()

p1.have_birthday_party()

p1.say_hi()
p2.say_hi()
p3.say_hi()

Person.say_hi()
Person.say_hi()
Person.say_hi()

print(p1)
print(p2)
print(p3)





