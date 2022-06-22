#Functions
def hello():
    print("hello")
    print("hello again")
hello()

hello()

print()
# Function with Main
def getInteger():
    result = int(input("Enter Integer:"))
    return result
def Main():
    print("Started")
    output = getInteger()
    print(output)
if __name__=="__main__":
    Main()
