# For Loops
for step in range(5):
    print(step)

print()
# While loops
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print()
# Modules

import math
def Main():
    num = -85
    num = math.fabs(num)
    print(num)
if __name__=="__main__":
    Main()
