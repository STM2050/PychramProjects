# Method 1
import calendar as c

yy = 2022
mm = 12

print(c.month(yy, mm))

print()

#Method 2
import calendar as c

yy = int(input("Enter year:"))
mm = int(input("Enter month:"))

print(c.month(yy, mm))

print()

import calendar as c
print("The calendar of year 2022:")
print(c.calendar(2022, 2, 1, 6))

