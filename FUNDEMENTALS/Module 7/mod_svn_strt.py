# INTRODUCTION
# comprehension
# iterable objects and iterators
# lazy evaluation with generators
# other tools used when working with iterable objects

# LIST COMPREHENSIONS
# syntax for describing:
# - lists
# - sets
# - dicts
# done in a declarative and functional style
# makes it readable and expressive
# making it able to effectively communicate intent to human readers
# readable - expressive - effective
# some comprehensions almost read like natural language
# this makes them almost self documented and can be documented nicely
# list comprehensions
# EX:
words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
# comprehension is enclosed in square brackets
# instead of an element in the brackets, it contains code to declare the elements of a new list
# inside those brackets logic is applied to form the new list comprehension
print([len(word) for word in words])
# general form is:
"""
[ expr(item) for item in iterable ]
works by looping through an iterable (ex: list) and taking each iteration -
 - and applying an expression that will output another value (len, abs, in(membership), etc)
"""
# the iterable can any iterable object, list, tuple, etc
# for each item in the iterable on the right, we evaluate it on the left (in terms of the item)
# use that evaluation as the next item in the new list, .append() on
# this comprehension is equivalent to:
lengths = []
for word in words:
    lengths.append(len(word))
print(lengths)
# the expression can be any python expression
# for example a factorial is the number it is multiplied by the product of all whole numbers down to 1 below it
# we then use this method for each number in range 0-19 to then convert it to a string and then find the length
# finding the power by, 10s(1), 100s(2), 1000s(3), etc...
from math import factorial

f = [len(str(factorial(x)))for x in range(20)]
print(f)
# type of object produced by list comprehensions is just a regular list
print(type(f))

# SET COMPREHENSION
# set supports a similar comprehension but instead of brackets [] it uses curly braces {}
"""
{ expr(item) for item in iterable }
uses the iterable to loop through to then use each item in it to be evaluated with the expression -
- to produce an output for that iteration of the iterable
works the same as the list comprehension but this removes any duplicates - 
- though it will not be stored in an order because sets are unordered sequences
"""
# EX:
print({len(str(factorial(x))) for x in range(20)})

# DICTIONARY COMPREHENSIONS






