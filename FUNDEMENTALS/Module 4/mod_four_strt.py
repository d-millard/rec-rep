# INTRODUCTION
# references to objects
# EX:
"""
x = 1000
python creates an int object of 1000 and sets it to the reference of x
"""
# int objects are immutable and cant be changed
# EX:
"""
x = 500
the int object of 1000 isn't changed but another int object of 500 is created and x 
is now assigned to reference it

now with no way of reaching the int 1000 object the python garbage collector will now remove it
"""
# when assigning one variable to another it is just passing a reference to the int object
# EX:
"""
y = x
y is not equal to x itself but is passed the reference to 500

x = 3000
with x now being reassigned, y still equals 500 and x 3000 requiring no work from the garbage collector
"""
# id() - returns a unique identifier for an object
# returns an integer identifier that is unique/constant for the lifetime the object set to
a = 496
print(id(a))
b = 1784
print(id(b))
print(id(a) == id(b))
b = a
print(id(b))
print(id(a) == id(b))
# is operator tests for equality of identity
print(a is b)
# augmented assignment operator changes id
b += 2
# augmented assignment creates an int 5 object then another int object of 2
# then adds them together and sets the variable equal to an int object of 7 with remaining objects garbage collected
print(a is b)
# since lists are mutable
r = [2, 4, 6]
s = r
s[1] = 17
print(r)
print(s is r)
# since s is referring to the same object as r changing either changes both
# id() deals with object not the references within it
# python doesn't have variables but just references to objects
p = [4, 7, 11]
q = [4, 7, 11]
# p and q are references to two different objects with identical value
# but since they are different objects their ids differ
print(p == q)
print(p is q)
# value equality vs identity
# value - equivalent "contents"
# identity - same object
# value comparison can be controlled programmatically
# when controlling types, can control how class determines value equality - can control the values and types
# identity comparison is defined by language and cant control behaviour

# ARGUMENT PASSING
# there isn't a copy of the argument passed into the function
# the argument is just a reference to the same object created from outside the function
# if a copy is need the function must create it
# EX:
# a function that modifies a list
m = [9, 15, 24]


def modify(k):
    k.append(39)
    print("k = ", k)
    return k


z = modify(m)
print(z is m)  # true because it is just changing values of object in reference
# when passing something into a function, if the object is replaced (not just changed)
# it will not change the one outside, leaving the inside as a new object
# reassigned reference g from the f list object to the new list object
# EX:
# function that replaces list, not just change (new list object)
f = [14, 23, 37]


def replace(g):
    g = [17, 28, 45]
    print("g = ", g)
    return g


h = replace(f)
print(f)
print(h)
print(h is f)  # false because of new object
# though you can completely change to values of list outside a function by modifying each individual element


def replace_contents(g):
    g[0] = 17
    g[1] = 18
    g[2] = 20
    print("g = ", g)
    return g


h = replace_contents(f)
print(f is h)  # True because the values have been changed but object remains same
# function arguments are passed by object reference
# the reference is copied but not the actual value of the object
# return returns a reference as well
# EX:


def f(d):
    return d


c = [1, 2, 3]
e = f(c)
print(e is c)  # True because the return just passed the reference onto the variable e

# FUNCTION ARGUMENTS IN DETAIL
# default function - sets the default value from an argument if not specified
# the parameters with defaults must come after those with defaults
# EX:
"""
def function(a, b = value):
"""
# EX:


def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("banner_test_one")
banner("banner_test_two", "*")
# the message string is a positional argument while the border string is a keyword argument
# the positional arguments are matched in position and sequence while the key words are matched with names
# EX:
banner("banner_test_thr", border="#")
# if all keyword arguments are used any order is allowed but if positional is required they must go after it
# EX:
banner(border="=", message="banner_test_fou")
#
# EX:
import time
time.ctime()


def show_default(arg=time.ctime()):
    print(arg)


show_default()
# if the repl was used, the show_default will always output the same time
# this is because the function creates an object once with the default argument
# with the arg keeping the same reference every time
# default argument values are evaluated when the def is evaluated
# they can be modified like any other object
# using mutable collection as argument defaults causes this problem bc the default is evaluated once
# but the collection produces different objects
# EX:


def add_spam(menu=[]):
    menu.append("spam")
    return menu


breakfast = ['bacon', 'eggs']
print(add_spam(breakfast))
lunch = ['baked beans']
print(add_spam(lunch))
print(add_spam())
print(add_spam())
print(add_spam())
# the default argument object is modified with the object staying the same but being modified
# this means the reference object changed but since it is still the object, it is evaluated as if it was the same
# EX:


def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


print(add_spam())
print(add_spam())
print(add_spam())
# to work around this issue use a immutable object like non and test if it is the same object
# if so set the default to that argument

# PYTHON'S TYPE SYSTEM
# python has a dynamic and strong type system
# dynamic is object types are only resolved at runtime - doesnt need to be specified when written
# EX:


def add(a, b):
    return a + b


print(add(4, 7))
print(add(3.1, 4.8))
print(add("test", "ing"))
print(add([1, 32.0], [9.9]))
# this illustrates how not type is specified, but while the program is run
# the two arguments can reference any type of object
# a strong type system is where there is no implicit type conversion
# EX:
"""add("test", 45.0)"""  # doesnt work because python will not implicitly convert either to add
# the exception is to bool for if statements and while loop predicates

# VARIABLE SCOPING
# variables are untyped name declarations for objects
# they can be rebound or reassigned
# scopes are contexts in which named references can be looked up
# 4 scopes from narrow to large are
"""
LEGB rule
local - inside the current function

enclosing - any and all enclosing functions

global - top level of module

built-in - provided by the builtins module
"""
# module scopes are usually from imports or functions
# local scopes are brought as variables, arguments, and items (in a list)
# EX:
count = 0


def show_count():
    print("count = ", count)


def set_count(c):
    global count
    count = c


show_count()
# didnt work because it binds count locally
# creates a new variable that shadows that of the global meaning the global one is not bound
# to avoid this must use the count name to declared witch to bind it to
set_count(5)
show_count()

# EVERYTHING IS AN OBJECT
# primitive objects, functions, modules  ==  all objects
# the import and def keywords bind an object to the name in namespace
# use type() to find any type of object something is
# use dir() to see attributes of objects

# TESTING
# time_testing.py

