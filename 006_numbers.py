# The two built-in types of numbers in Python are int and float.
# Ints are whole numbers and floats are decimal numbers.
#
# Both number types support addition (+), subtraction (-), multiplication (*), division (/) and more.
#
# Division always results in a float, even if the result would be a whole number
# (e.g. 10 / 2 will give you 5.0).
#
# round() is a built-in function that will round a float to the nearest whole number.
#
# Dividing by zero will result in a ZeroDivisionError exception.
#
# You can create integers using the int() function. You can create floats using
# the float() function. Using int() on a float is not the same as using round() on one.

print(5 + 5)
print(2 - 2)
print(10 * 18)
print(8 / 2)

# print(10 / 0) # ZeroDivisionError: division by zero

print(5.0 + 2.5)
print(1.2 + 0.3)

print(0.1 + 0.1 + 0.1 - 0.3)

print(round(0.1 + 0.1 + 0.1 - 0.3)) # round() rounds a float to the nearest whole number

print(int(5.2)) # returns 5
print(int(5.9)) # returns 5
# int() chops off the deciaml, and turns strs into ints if str is numeric
print(int("5"))

print(float("5.2")) # returns 5.2

print(5 + 5 * 2) # returns 15 due to bedmas
print((5 + 5) * 2) # returns 20

a = 5
a += 1 # same as a = a + 1
print(a) # returns 6
a -= 1 # same as a = a - 1
print(a) # returns 5
