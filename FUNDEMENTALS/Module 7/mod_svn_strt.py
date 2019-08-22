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
# uses curly brace like the set comprehensions
# distinguished by the key and value expressions
# set and dict are both mutable sequences of immutable objects
# but with dict the key is only iterated through and cannot be altered but the value can
# format:
"""
{key_expr:value_expr for item in iterable}
"""
# EX:
from pprint import pprint as pp
# dict declared
# dictionary inversion for quick lookups in opposite direction
# in this case it would allow countries to now be the values
country_to_capital = {'Uk': 'London',
                      'Brazil': 'Brazilia',
                      'Morocco': 'Rabat',
                      'Sweden': 'Stockholm'}
# iterating over general dictionaries isn't too effective because it yields only the keys
# the .items() method allows it to be done with the key value pair combined with tuple unpacking
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)
# if comprehension produced identical keys, the later key value pairs will always override earilier ones
# if a key is declared early with a value, then a later key is declared with a value
# both the key and value are replaced with the same key but different value
# values can be the same as many times though
# EX:
# in this case only the hotel key value pair is kept because the other h words were overridden
# because hotel was the the latest one
words = ["hi", "hello", "foxtrot", "hotel"]
pp({word[0]: word for word in words})
# it is best practice to not cram too much complexity into comprehensions
# EX:
# this example reaches the limits of the complexity of comprehensions
# this example finds the files in your current working directory and creates a dict
# the path is the key and the size of the file in that path is the value
# this works with os.path.realpath(file) finding the path
# then with os.stat(file).sst_size getting the size of the file
# then with this being looped with glob.glob('*.py') that looks for any (* - means anything before it).py file
# in current working directory
import os
import glob
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)

# FILTERING PREDICATES
# all 3 types of comprehensions previously talked about support an optional filtering clause
# this uses an if statement to filter out anything as long as the if is true
# this allows us to "filter" things into a comprehension
# format:
"""
[expr(item) for item in iterable if predicate(item)]
this then means for the iterable, each item true with the predicate, it evaluate with expression
and then be added to the construct
this option works with:
list - set - dict comprehensions
"""
# EX:
from math import sqrt


def is_prime(num):
    if num < 2:
        return False
    # uses sqrt + 1 because range go up to the index before the final number
    # this means in this cas it will go up to the sqrt because it is to the sqrt + 1
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# the expression now instead of right to left to:
# middle - right - left
# iteration first - test for true predicate second - evaluate expression last
# for range, if just 1 thing is input it is the end and starts with 0
# range(fir, sec, thi)
# - fir being where to start: optional
# - sec being where to end: not optional
# - thi being how many to go by 1, 2, 3, etc... each iteration: optional
# in this evaluation the item is just added to the list and not evaluated with an expression
print([item for item in range(101) if is_prime(item)])
# can then use filter with an expression
# creates a dict of the prime number squares, key is the squared number, value is numbers that are divisions of square
# this shows another way to use comprehensions because a expression can just be x*x as key with (1, x, ...) tuple value
# comprehension don't have to just be something that has an output of a number but any transformation of a value
# it can just be item, the item with a work after, f"this is the number: {num}", anything that follows format of comp
"""
all the prime numbers square to be the whole number square roots
"""
prime_square_divisors = {x*x: (1, x, x*x) for x in range(101) if is_prime(x)}
pp(prime_square_divisors)
# testing:


def if_convert_float(num):
    try:
        float(num)
        return True
    except (ValueError, TypeError):
        return False


num_in = ["5.003", 623, 23.04, [4.22], {"hey": 32.2}, "33", -1222.23, -1]
floats = [{"number": num, "format": f"({type(num)}), square = {float(num)*float(num):.2f}"}
          for num in num_in if if_convert_float(num)]
pp(floats)

# USEFUL ZEN
# sometimes a complex comprehension is worse than than the corresponding for each loop
# functional, no side-effects (runtime effects like printing and running anything)
# if side-effects are need a for loop would be better way to go
# use comprehensions for strictly non-complex construct building

# ITERATION PROTOCOLS
