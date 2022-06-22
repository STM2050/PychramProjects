print("Enter four numbers and then I will tell which is greater")
num1 = int(input("Enter First number:"))
num2 = int(input("Enter Second number"))
num3 = int(input("Enter Third number"))
num4 = int(input("Enter Fourth number"))

if (num1>num2) and (num1>num3) and (num1>num4):
    print(num1, "Greater")
elif (num2>num1) and (num2>num3) and (num2>num4):
    print(num2, "Greater")
elif (num3>num1) and (num3>num2) and (num3>num4):
    print(num3, "Greater")
else:
        print(num4, "Greater")