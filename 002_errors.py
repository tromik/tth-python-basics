# name error - something being used or called doesn't exist as far as python
# is concerned

# print(5 + x)
#
# results in the following:
# Traceback (most recent call last):
#   File "002_errors.py", line 4, in <module>
#     print(5 + x)
# NameError: name 'x' is not defined

# call_best_friend()
#
# results in the following:
# Traceback (most recent call last):
#   File "002_errors.py", line 12, in <module>
#     call_best_friend()
# NameError: name 'call_best_friend' is not defined


# type error - either gave wrong type to a function or tried to do something
# with a type that the type doesn't supper

# print(5 + 'a')
#
# results in the following because a letter (string) cannot be added to a number:
# Traceback (most recent call last):
#   File "002_errors.py", line 24, in <module>
#     print(5 + 'a')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# syntax error - python doesn't understand what you are trying to do

# print("Hello)
#
# results in the following because the close quote is missing:
#   File "002_errors.py", line 35
#     print("Hello)
#                 ^
# SyntaxError: EOL while scanning string literal
