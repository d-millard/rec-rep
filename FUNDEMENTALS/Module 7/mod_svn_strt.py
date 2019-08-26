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
floats = [{"number": num, "format": f"({type(num)}), square = {float(num)**2:.2f}"}
          for num in num_in if if_convert_float(num)]
# pp(floats)
print()
for item in floats:
    (_, number), (_, form) = item.items()
    print(f'{number}:\n\t{form}')
print()

# USEFUL ZEN
# sometimes a complex comprehension is worse than than the corresponding for each loop
# functional, no side-effects (runtime effects like printing and running anything)
# if side-effects are need a for loop would be better way to go
# use comprehensions for strictly non-complex construct building

# ITERATION PROTOCOLS
# comprehension and for loops are most frequently used when performing iteration
# this is the act of taking each item in a series one by one and doing an evaluation upon it
# though these iterations iterate over the series as a whole
# though sometimes a fine grained controller may only want part of it
# two concepts:
"""
iterable protocol:
this is the collection/data structure that can be iterated through, list, dict, set...
this gets an iterator from within the iterable
iterator is an object of an iterable that traverses the iterable iterated -
- this allows the movement through the sequences of the iterable
can be passed to built in iter() function to get an iterator
format - iterator = iter(iterable)
iterator protocol:
this is the item being in the iterable object, the items being iterated over
all this does is get the next iterator in the series
this is a iterable and can be used to get sequences in other methods like comprehensions and loops -
- though it is not a collection type because it is more of a iterable collection type being looped through itself -
- with the references to all the sequences within it but with no series itself
can be passed to built in next() function to fetch the next item
format - item = next(iterator)
"""
# every iterator is a iterable but not every iterable is a iterator
# a list is not an iterator but a list iterator is a list
# an iterator is an object from a collection that allows to traverse the sequences in the now iterator iterable
# EX:
# the example shows the iterable is the series and each item in it is an iterator

iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
# each call of next to iterator moves it to next in sequence
# the iter() returns a iterator which can be used to move through the iterable sequence that the iterator references
iterator = iter(iterable)
print(len(iterable))
"""
this means you can loop through an iterator like you would with an iterable
both are the same object so similar roles can be done with either
for r in iterator:
    print(r) # prints each sequence in iterator
print(len(iterable)) does not work same as print(len(iterator))
even though the iterator is an iterable it does not support protocols like size
this is because they are used as a way to move through the iterable object referenced 
but not as a direct copy of the iterable but a separate object that is a iterable with the ability to step through
"""
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(iterator)
print(next(iterator))
# when getting to end of iterable with next() function a StopIteration exception is raised
# print(next(iterator))  throws a stopIteration error
# EX:
# in this cas it is possible to get an iterable and return the first iterator in the series
# if it is empty a StopIteration will be raised and therefore can be handled to represent an empty iterable


def first(iterable):
    try:
        return next(iter(iterable))
    except StopIteration:
        print("iterable is empty")
        # raise StopIteration("iterable is empty")


print(first({4, 5}))
print(first([2, 93, 2]))
print(first([]))
# high level loops and comprehensions use this low level method
# true definition -
"""
an iterator is an object with a reference to the iterable with the iter() function
it then uses this reference to output all sequences of the iterable
it does this by every iteration going to the next item and saving its point as its new starting point -
- in the next iteration
it cannot go in any direction - when it gets to end it raises a StopIteration error
EX:
image this like a class that has iter() return the iterable to itself
then using the next() to start at the first point and increase 
index_of[x]
x = x += 1
"""
# testing example:


class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            temp = self.data[self.index]
            self.index += 1
            return temp
        except IndexError:
            raise StopIteration


def func_iterate(user_in, sequence=None):
    if sequence is None:
        sequence = []
    it = Iterator(user_in)
    try:
        while True:
            sequence.append(it.__next__())
    except StopIteration:
        return sequence


print(func_iterate("print_dis"))

# GENERATORS
# specify iterable sequences
# - all generators are iterators
# - meaning they go from one sequence to another on iterable of reference
# are lazily evaluated
# - next value in the sequence is computed on demand
# - only run code when requested to
# can model infinite sequences
# - such as data streams with no definite end
# - can go forever unless sentinel/signal is sent to stop
# able to make seamless combining pipelines
# - for natural stream processing
# - this means when one generator feeds another data when requested,
# - allowing a stream of conversions to take place from one generator to another
# defined as:
"""
any function that uses that yield keyword at least once (can be used more than once)
format:
yield value
may also have return keyword with no arguments
this will most likely be to signal to stop the function from yielding anymore values
like any function there is implicit return at end, (expected)
"""


def gen123():
    yield 1
    yield 2
    yield 3


# generator function is treated exactly like an iterator object
# it is an object that will iterate when told until stopped at any point
# the generator object is exactly an iterator object
# though in its case, its iterable sequence as is its yields
# this differs itself from an iterable because the yield can continue to any amount wanted
# uses next() like a regular iterator
g = gen123()
print(g)
print(next(g))
print(next(g))
print(next(g))
# works same as going over with an iterator
# a stopIteration error is raised when there is no more to yield
# print(next(g)) # stopIteration error is raised
# because generators are an iterator it is as a iterable meaning it can be used in the typical iterable ways
"""
prints all sequences yielded from generator function as if they were sequences in a list
able to be used in comprehension and loops as well 
for r in gen123():
    print(r) 
[print(r) for r in gen123()]
"""
# each call to the generator function returns a new object iterator
# this is because it is a new object being made each time because the yielded iterator sequences are new objects
# making it together a new object
# EX:
h = gen123()
i = gen123()
print(h)
print(i)
print(h is i)
# this can be shown through using one to move does not affect the others
# independent movement
print(next(h))
print(next(h))
print(next(i))
# more advanced tracking on complex generator to view what is going on
# EX:
# the final statement is about the implicit return at the end of every function
# if no more possible computation can be done


def gen246():
    """

    """
    x = 0
    x += 2
    print('About to yield 2')
    yield 2
    print('About to yield 4')
    yield 4
    print('About to yield 6')
    yield 6
    print('About to return')


# the code executes just far enough to yield value
# once value called for is yielded, block stops execute but stays waiting at yield to continue execution
g_list = gen246()
print(next(g_list))
print("__yield next value__")
# this shows how the generator function stayed at the first yield 2 and waited for further execution
# yield is like a return for the function but remembers where it was returned and can be called to further function -
# - from that point
# iterators remember starting point and set every new iteration point as new starting point
# could be like each yield is an increasing index
print(next(g_list))
print("__yield next value__")
# the function resumes again, each yield is like a pause on the function
# when called for next yield value it resumes where it left off
print(next(g_list))
print("__yield final value__")
# once function gets to end of body with not more yields a StopIteration is thrown like every Iterator
# print(next(g_list))  # raises StopIteration

# STATEFUL GENERATOR FUNCTIONS
# generators need to be treated like objects
# once a generator object reference is created then it can be used
# generators cannot be used as regular functions
"""
generators resume execution
- when a yield is reached, instead of ending the function 
- the function pauses and resumes when next yield is requested
- ends when can no longer supply values or no values are requested
can maintain state in local variables
- work as standalone functions with blocks of variables and functionality
complex control flow
- allowing it to be resumed and paused continuously
- allowing it to be ended with return
lazy evaluation
- evaluate to a yield only when requested, pauses once supplied 
- then resuming from pause point
"""
# create a pipeline (generators feeding other generators to get continuous conversions)
# pipeline_exercise.py  # example used
# to display debugger mode and a generator pipeline
# to use debugger mode use breakpoints on sections of code that want to see
"""
continue
finishes current iteration of loop and begins the next immediately
works with most loops, while - for
"""
"""
MAKE SOME PIPELINE STUFF IN TESTING
"""

# LAZINESS AND THE INFINITE
# generators are lazy meaning computation are happened just in time when next result is requested
# - meaning blocks of logic and computations are only ran when a value is requested, they then stop when it is yielded
# - but then finish/resume when another is requested
# this means they can be used to model infinite sequences
# values are only produced as requested by called
# - can continuously call elements and generator will continuously produce values
# no data structure needs to be built to contain elements
# - each element is yielded individually meaning a data structure wouldn't be needed just the constant output of values
# this allows them to be useful in sensor readings, infinite or large, mathematical series, massive files...
# fibonacci or quick sort - maybe test
# lucas() series,
# EX:
# this series produces the sum of the two proceeding values


def lucas():
    # its starts with yielding 2
    yield 2
    a = 2
    b = 1
    while True:
        # it then yields b
        # from there it uses tuple unpacking to set a to the now previous b
        # and b to the the now previous a and itself (b)
        # this works as a always being a reference the number in the iteration 2 before and b being the number 1 before
        # though once unpacked - a is 1 behind and b is the value of that iteration
        # they then are updated each request to increase 1 place each but still staying 2 and 1 before
        yield b
        a, b = b, a + b


for i, v in enumerate(lucas()):
    # if cannot exit terminate program some how
    if i >= 101:
        break
    print(v)

# GENERATOR
# generator comprehensions
# these expressions are a cross between comprehensions and generator functions
"""
similar syntax to list comprehensions
- similar syntax to list comprehension just with the [] replaced with ()
create a generator object
- instead of returning a collection it returns an generator iterator that can then be used
concise
- can turn general iterators into other generator object with special evaluation and filters
lazy evaluation
- works the same as using the yields from the generator but instead each yield passes through filter and evaluation
- lazily evaluates
- (if does not pass filter, the expression goes back to yield another until it itself can yield)
"""
# testing stuff:


def square():
    k = 0
    while True:
        yield k
        k += 1


def overlap(even, odd):
    for e, o in zip(even, odd):
        yield e
        yield o


def run():
    even_squares = (k * k for k in square() if k % 2 == 0)
    odd_squares = (k * k for k in square() if k % 2 != 0)
    three_digit_squares = (k for k in overlap(even_squares, odd_squares))
    for index, value in enumerate(three_digit_squares):
        if len(str(value)) > 3:
            break
        elif len(str(value)) == 3:
            print(value)


run()
"""
syntax
(expr(item) for item in iterable (optional if filter))
like a list and set but is delimited by parenthesis ()
"""
# EX:
# an object can be created of a generator to yield values that are evaluated
hundred_squares = (x * x for x in range(101))
print(hundred_squares)
print(list(hundred_squares))
# once the object generator has been used (yielded everything)
# it cannot be reused because it has yielded everything possible
# generators are single use objects
# this is because they yield until they are unable to, once unable to the code is unusable
# - in this case think about it waiting at the yield of 100, once called again the object is the same
# - so it is still waiting at the 100 yield and because the range is until there, it won't yield anymore elements
# - the same generator will always pause and resume
print(list(hundred_squares))
# though you can recreate this generator by assigning the expression to another object
hundred_one_squares = (x * x for x in range(102))
print(list(hundred_one_squares))
# EX:
# sum of 10 million numbers
# if generator expression is contained in function, the use of the parenthesis are optional
# this consumes significantly less memory due to the fact that each number yielded is terminated after evaluation
# in the case of list, each number would have to be stored then summed
# with a generator iterator it wil use the number and then forget about it meaning just the sum is stored
# in expression, separate enclosing parenthesis aren't used to distinguish generator expression
# like tuple, parenthesis are optional in sum cases
print(sum(x*x for x in range(100001)))
# can also use if filter predicate
print(sum(x*x for x in range(100001) if is_prime(x)))

# BATTERIES INCLUDED FOR ITERATION
# any object that follows iterable or iterator protocol can be used for iteration
# common built in functions for iterator operations
# these functions provide the core of how iterators can be used
# these allow very precise, concise, and readable code
"""
some met so far are
enumerate
- produces an index with value
sum
- sums together iterable (an iterators values) of all iterations
"""
# on top of built in functions -
# - itertools (module) provides many other useful functions and generators to process streams of data
# EX:
# solving first sum of 1000 primes function using islice() and count() generators
from itertools import islice, count
"""
islice(iterable, amount)
- perform lazy slicing similar to list functionality 
- first is iterable 
- second second is the amount to stop slicing at
- can be used to stop generator at set amount of yields
count()
- continuously generates a count of numbers 1, 2, 3, etc...
"""
thousand_primes = sum(islice((x for x in count() if is_prime(x)), 1000))
print(thousand_primes)
# two useful built in operators any and all
# any is like or, checks if at least one iteration is evaluated to True
# all is like and, checks if all iterations are evaluated to True
# used on series of bool values
# EX:
print(any([False, False, True]))
print(all([False, True, True]))
# tests if any numbers in that range are prime
print(any(is_prime(x) for x in range(1328, 1361)))
# used to test if all square in a certain range are square
# little bit of testing:
# in this test the square generator is used to generate an infinite list of squares and is then tested to see if all
# are true in the range 0 - 100
# zip is then used to end it at 100 with the infinite test_square generator
# then the all keyword is used to test if the range_test has all True iterations
test_square = ((True if i * i == v else False) for i, v in enumerate(k * k for k in square()))
range_test = (test for _, test in zip(range(101), test_square))
print(all(range_test))
# last useful tool is zip :
# (just used this found out about it with research on how to iterate through two series for venn diagram)
# - synchronize iterations over multiple iterable series
# - ends both when one stops producing values
# EX:
sunday = [12, 14, 15, 17, 21, 22, 22, 23, 22]
monday = [12, 14, 14, 16, 20, 21, 22, 22, 23]
thursday = [12, 14, 15, 17, 21, 21, 22, 22, 23]
# zip produces a tuple of all values
for item in zip(enumerate(sunday), monday, thursday):
    print(item)
# tuple unpacking can then be used to get the individual elements
for i_o, i_t, i_r in zip(enumerate(sunday), monday, thursday):
    print(f"item one = {i_o}, item two = {i_t}, item three = {i_r}")
# the tuple returned from zip can use other built ins, min(), max(), sum(), abs(), len()
# in this case we can output the min max and sum/len or average using these built ins
for temps in zip(sunday, monday, thursday):
    print(f"min={(min(temps)):.2f}, max={(max(temps)):.2f}, average={(sum(temps) / len(temps)):.2f}")
# though if one long iterable series to iterate through
# chain:
# lazily concatenates multiple series and iterates through all iterations
# better than actual concatenation because instead of duplicating the data into an iterable, it makes an iterator
# return an iteration of each element
from itertools import chain
# chains together all series to an iterator of all the data of each
temperatures = chain(sunday, monday, thursday)
# an iterator object
print(temperatures)
t = (t for t in temperatures)
# each data in each list in order of how they were input
for k in t:
    print(k)
# the evaluate can use truthy and falsely as evaluations too
print(all(t > 0 for t in temperatures))
# final lucas brings together everything learned
# it show cases the use of filter predicates, infinite generators with generator comprehensions
# and built in iteration tools like enumerate used with tuple unpacking
# this uses the lucas() gnerator to generate numbers of the two numbers before it then filtered by primes
# then yielded by generator comprehension to be requested by for loop to be printed out
for index, x in enumerate(p for p in lucas() if is_prime(p)):
    if index > 10:
        break
    print(x)


# TESTING
# look up a video explaining quick sort
# pipeline
# quick sort maybe








