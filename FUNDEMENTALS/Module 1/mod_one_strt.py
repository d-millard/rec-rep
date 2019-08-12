# REPL
# repl is only in the python console
"""
read
evaluate
print
loop
"""

# HELP COMMAND ON REPL
# type help() with anything inside the parenthesis in repl to see information about
# functions, classes, etc
# press q to leave help browser

# WHITESPACE IN PYTHON
# python uses indentation levels to demarcate code blocks
# 4 spaces a level
# 1. requires readable code
# 2. no clutter
# 3. human and computer can't get out of sync
# prefers 4 spaces
# never mix spaces and tabs
# be consistent on consecutive lines
# only deviate to improve readability

# PYTHON CULTURE AND ZEN
# zen of python is guiding principle of python
# see it on python documentation or by on repl typing "import this"

# IMPORTING FROM THE PYTHON STANDARD LIBRARY
# use "import module_name"
# use the import with a .func_name()
import math

# sqrt returns a float
print(math.sqrt(81))
print(math.factorial(5))
# to get the amount of fruit drawn form a pile of 5 would be
n1 = 5
k1 = 3
# the factorial of total over the product of the amount taken out and the difference of both factorials
print(math.factorial(n1) / (math.factorial(k1) * math.factorial(n1 - k1)))
# instead of using import can use "from module_name import func_name"
from math import factorial

print(factorial(n1) / (factorial(k1) * factorial(n1 - k1)))
# finally can be renamed when imported with "from module_name import func_name as var"
from math import factorial as fac

print(fac(n1) / (fac(k1) * fac(n1 - k1)))
# the / operator is pythons floating point division operator and returns a float when used
# pythons // operator is integer division operator and returns an int when used
print(fac(n1) // (fac(k1) * fac(n1 - k1)))
# python doesnt have a maximum number
# limited by computer memory
print(fac(50))

# SCALAR TYPES
# int arbitrary precision integer
# float 64 bit floating point numbers
# None - null object
# bool - boolean logical values
# int
# 10 = 10
# binary 0b10 = 2
# octal 0o10 = 8
# hexadecimal 0x10 = 16
# convert to int with int()
print(int("1000"))
print(int(3.6))
# float
# 15 to 16 significant digits
# scientific notation can be used 1.616e-10
# use float() to convert to float
print(1.616e15)
# use nan for not a number float("nan")
# inf for infinity float(inf)
# -inf for negative infinity float(-inf)
# any calculation with float and int will result in float
# None
# can test for None
# bool
# True and False
# for int
# use bool() to convert to bool
# with ints and float, anything other than 0 will be true
print(bool(0))  # will be false
print(bool(42))  # will be true
print(bool(-1))  # will be true
print(bool(0.0))  # will be false
print(bool(0.0207))  # will be false
# an empty list will be false
print(bool([]))
# empty string will be false
print(bool(""))

# RELATIONAL OPERATORS
# returns True if statement is correct and False if incorrect
g = 20
# == value equality
print(g == 20)  # True
# != value inequality
print(g != 20)  # False
# < less than
print(g < 19)  # False
# > greater than
print(g > 19)  # True
# <= less than or equal to
print(g <= 21)  # True
# >= greater than or equal to
print(g >= 20)  # True

# CONDITIONAL STATEMENTS
# if statements
# the expression is converted bool by bool() constructor
# bool() constructor isn't needed because that's what the if already does
# else occurs when the if expression is false
# if ... elif ... else
a1 = "eggs"
b1 = "man"
if a1:
    print("if true1")
elif b1:
    print("elif true2")
else:
    print("if false3")
# elseif keyword
# same as else if keyword

# WHILE LOOPS
# the expression is converted bool by bool() constructor
# bool() constructor isn't needed because that's what the while already does
# -= subtracts equals
# += adds equals
# *= multiply equals
c1 = 5
while c1 != 0:  # 0 == False, could just check for c1 falsely but too implicit
    print(c1)
    c1 -= 1
# if in a infinite loop in repl press "ctrl + c"
# break keyword terminates the innermost loop, transferring execution to first loop
# in example the break terminates the while but if that while was nested control would go to after parent loop
# after going to parent it will then finish the iteration of that loop after what follows the loop
while True:
    response = input("Input a number")
    if int(response) % 7 == 0:
        break

# TESTING
# could data validate like
while True:
    res = input("Please input a whole number: ")
    if res.isdigit():
        break
print(res)
# or better validation
while True:
    res = input("Please input a number: ")
    try:
        if int(res):
            break
        elif int(res) == 0:
            break
    except ValueError:
        ""
    try:
        if float(res):
            break
        elif float(res) == 0.0:
            break
    except ValueError:
        ""
print(res + " first")


# in function form - returns the number instead of the string
# could work if a true was returned from true statements and false from the exceptions
# then used to change a flag in a loop and keep going until the function made the flag true
# meaning the number was value


def number_validate():
    while True:
        num = input("Please input a number: ")
        try:
            if int(num):
                return int(num)
            elif int(num) == 0:
                return int(num)
        except ValueError:
            ""
        try:
            if float(num):
                return float(num)
            elif float(num) == 0.0:
                return float(num)
        except ValueError:
            ""


print(str(number_validate()) + " second")
