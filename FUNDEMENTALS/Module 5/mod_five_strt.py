# INTRODUCTION
# str or string - immutable sequence of unicode code points
# list - mutable sequence of objects
# dict - the mutable mapping of immutable keys to mutable key objects
# tuple - the immutable mapping of objects
# range - arithmetic progressions of integers
# set - a mutable collection of unique immutable objects

# TUPLE
# immutable sequence of objects
# once created the objects within can be replaced or removed
# new elements can not be added
# same format as list but delimited by ()
# EX:
t = ("Test", 333, 9.03)
print(t)
# access elements with 0 based index
print(t[0])
# use len() to get length
print(len(t))
# iterate with for loop
for item in t:
    print(item)
# concatenate with +
t = t + (7.0, 6.43)
print(t)
# can be repeated with *
print(t * 3)
# tuples can contain nested tuples
# EX:
a = ((9.0, 8.3), (5.0, "dsf"))
print(a)
# use repeated operation of index operator to get inner elements
print(a[1][1])
# when a single element tuple is needed
# the use of a trailing comma is needed to specify tuple
# this is because without it will be recognized as an int
# EX:
h = (324)
print(type(h))
k = (324,)
print(type(k))
# specify an emtpy element tuple just use empty parenthesis
e = ()
print(type(e))
# parentheses are optional for one or more elements
# EX:
p = 1, 2, 4
print(type(p))
# useful for multiple return values
# a tuple is the same as a return from a function
# EX:


def minmax(items):
    return min(items), max(items)


print(type(minmax([83, 33, 84, 32, 85, 31, 86])))
# tuple unpacking
# unpack data structures into named reference, in same order returned
lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])
print(f"{lower}, {upper}")
# works with arbitrarily nested tuples but not with other structures
# can be structure to tuple, but must be same elements and layers of nesting
(a, (b, (c, d))) = (4, (3, [2, 1]))
print(a, b, c, d)
# can swap variables
# set the order of the variables equal to the reverse order
# idiomatic python swap
# EX:
a = 'jell'
b = 'peanut'
a, b = b, a
print(type(a))
print(a, b)
# can use the tuple constructor to create a tuple from other series of iterable objects
# EX:
o = tuple([83, 33, 84, 32, 85, 31, 86])
print(o)
# strings can be done as well but each character is seen as an iterable with the string as the data structure
# EX:
y = tuple("testing the tuple".replace(" ", ""))
print(y)
# most collections allow the in operator to be used to test for containment
# not in therefor checks if it is not in the collection
# EX:
print(5 in (3, 5, 6))
print(5 not in (3, 5, 6))

# STRING
# homogeneous immutable sequence of unicode codepoints(characters)
# len() gives number of characters not on 0 based index
# EX:
print(len("hello my name is charles"))
# concatenation can be used to combine these strings to form one full sequence
# EX:
x = "new"
y = "found"
z = "land"
u = x + y + z
print(u)
# can also += to concatenate strings together to same variable
x += y
x += z
print(x)
# these methods aren't recommended on larger because it can take a toll on performance
# it is recommended to use the .join() method
# takes a collections of strings as an argument and produces a new string with separator between each of them
# the separator is specified by setting the separator as a string and then calling join on it
# EX:
x = '__'
colors = x.join(['#234', "#658568", "#9803"])
print(colors)
# or
colors = '__'.join(['#234', "#658568", "#9803"])
print(colors)
# it can then be split up again with the .split() method using the separator used in join
# without an argument the split divides it up by whitespace
colors1 = colors.split('__')
# or
colors2 = colors.split(x)
print(colors1, colors2)
# joining on an empty separator is fast way for concatenating a collection of strings
# when doing so it fully concatenated and no separator, no whitespace, is included
colors = ''.join(['#234', "#658568", "#9803"])
print(colors)
# .partition() is used to split a single string into 3 parts
# 1 being the prefix, before the specified separator
# 2 being the separator, the point where the string is split but is split from the string as well
# 3 being the suffix, the part after the separator
# a tuple is returned
# EX:
x = "unforgetable".partition("forget")
print(x)
# this is commonly used in tuple unpacking
first, separator, last = "David Millard".partition(" ")
print(first, separator, last)
# often _ variable is used for undesirable variables, like the separator returned
# this convention is supported in many tools
first, _, last = "David Millard".partition(" ")
print(first, last)
# .format() method formats the strings usefully
# mostly already known
# replacement fields with 0 based index, and is populated by assignment in the method
# EX:
thing = "me"
age = 12
print("The age of {0} is {1}.".format(thing, age))
# these fields can be used a number of times
print("The age of {0} is {1}. {0}'s birthday is soon.".format(thing, age))
# if the fields are used exactly once in the string and lined with each in the method call the integers can be omitted
print("The age of {} is {}.".format(thing, age))
# if keyword arguments are supplied to method call, replacement fields can be chosen by the keyword instead of index
print("The age of {person} is {old}.".format(person=thing, old=age))
# keys and indexes can be accessed in the replacement field with [] square brackets
# EX:
pos = (56.7, 324.67, 234.0)
print("the coordinates are x={0[0]} y={0[1]} z={0[2]}".format(pos))
# or the clean the code
print("the coordinates are x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos))
# attributes can be accessed through the replacement field with . dot followed by attribute name
# since a module is an object it can be passed into format and display its attribute
# EX:
import math
print("Math constants: pi={m.pi} e={m.e}".format(m=math))
# floating points can also be altered with a :._f collen dot followed by the number of floating points
# to find more rules/tricks like this check documentation
print("Math constants: pi={m.pi:.3f} e={m.e:.2f}".format(m=math))
# or a test
print(f"Math constants: pi={math.pi:.3f} e={math.e:.2f}")

# RANGE
# arithmetic progression of integers
# collection not really container
# created by calls to the range constructor
# usually just put the end element, the range will start at 0 if not input
r5 = range(5)
print(r5)
# sometimes used a loop counters
# stop value supplied to range is 1 past the the actual stop seeing how the output stopped at 4
# goes until the amount of integrations is complete
for i in r5:
    print(i)
# or
for i in range(5):
    print(f"{i} second")
# can also supply the starting value
for i in range(5, 10):
    print(i, range(5, 10))
# can also wrap the range constructor in a list constructor t force production of each item
for i in list(range(5, 10)):
    print(i, list(range(5, 10)))
# the half open attribute of range seems strange but is intended to allow the next range start where the other ended
# a step through argument can be added as well to dictate the integral succession taken to get from start to end
# this option goes after the end has been specified
# to used step the first value must be specified as well
for i in list(range(0, 10, 2)):
    print(i)
# range doesnt support keyword arguments
# it is unpythonic to use iteration over index base and always try to iterable over iterable objects such as lists
# if a counter is need it is preferred to use the . enumerate() method
# returns a pairs of tuples being the index and the second being the value for every item in structure (index, value)
# EX:
t = [324, 213, 5467, 123, 879]
for p in enumerate(t):
    print(p)
    print(p[0], "index")
    print(p[1], "value")
# this can then be improved with tuple unpacking
# assigning each part of the pairs of tuples
# enumerate has an optional argument that all where to start counting, doesnt affect index but what it pairs with values
for i, v in enumerate(t, 1):
    print(f"index = {i}, value = {v}")
# ranges aren't widely used in modern python

# LIST
# heterogeneous mutable sequence
# create list using syntax, add to end using .append(), and change and get at their values using [] square brackets
# to index sequences, this applies to tuples as well is to use positive or negative indexes
# positive from 0 to 1 less than len(), starting from beginning to end
# negative from -1 (last) to - len()(beginning), from end to start
# EX:
s = "show how to index into sequences".split()
print(s[-5])
# much more elegant than forward in cases
print(s[len(s) - 1])  # less elegant
# vs
print(s[-1])  # more elegant
# slicing allows the ability to get part of a list
# a start and stop is needed
# both are optional with either a start or stop making it either go from beginning to stop or start to end of list
# [x:y] a colon is used to start the slice with start before it and stop after
# the range is half open meaning like range it will stop 1 before the specified end
print(s[1:4])
# can also be combined with negative indexing
print(s[1:-1])
# these two list show the effectiveness of the half open range convention by showing why it goes 1 before
# and is then picked up by the exact start
# optional stop
print(s[3:])
# optional start
print(s[:3])
# it is also possible to omit both start and stop and just have a colon [:] to get the entire list
# important for coping because a new object is created and now just the reference being passed
# though the elements within these lists are the same objects so if any are modified in either, the other will be
s.append(["hey1", "hey2"])
full = s
print(full is s)
print(full)
full = s[:]
print(full is s)
print(full)
s[-1].append("jsdf")
# the s list's last object was modified
# the full list has the same reference to that object so its same object was modified as well
print(full)
# three ways to copy a list are;
# 1 full slice, list = list[:]
x = s[:]
print(x)
# 2 .copy() method, list = list.copy()
x = s.copy()
print(x)
# 3 list() constructor, list = list(list)
# preferred in many ways for working with any iterable series source and not just a list
x = list(s)
print(x)
# all of these methods though create a shallow copy meaning a new list with same object references
# do not copy referred to objects

# SHALLOW COPIES
# EX:
# using nested inner lists as mutable objects
a = [[1, 2], [2, 3]]
# under the cover in order:
"""
1 - the 1 and 2 integer objects are created, the elements in the first inner list are references to these objects
2 - two more int objects are created containing values 3 and 4, the second inner list holds these references
3 - the outer list is created holding references to the two inner lists
4 - the reference name a is bound to the outer list
"""
# when the list is copied, it merely copies the references to the same objects
# we get a copy of the same references
# b = a[:]
# b = a.copy()
# or
# this new copy of the list a is then bound to b
b = list(a)
# this means while b is a new list object, it is in fact holding the same objects as a
print(b is a)
# they do have equivalent values
print(a == b)
# they have the same inner list objects
print(a[0] is b[0])
# when one of a objects are replaced though, it does not affect b objects
a[0] = [8, 9]
print(b[0])
# but when an inner list in a is modified, same object, b contains the same object and has its same object modified
print(b[1])
a[1].append(7)
print(b[1])
# the final data structures are two separate lists both containing two inner lists
# both share the same reference to their second lists, but contain different first list objects
print(a)
print(b)

# LIST REPETITION
# lists support same string repetition with multiplication operator, same as tuples
# this repetition returns a list of all the amount of repeated elements in list
# EX:
c = [21, 56]
d = c * 3
print(d)
# new objects are not created with the references just being multiplied
# meaning the new list would have multiple of the same objects
print(d[0] is d[2])
# it is rarely seen like that
# most often used to initialize a list to a known size with a constant value, 0 or None
# the same thing occurs with the constant being the same object as all other created elements
# they are same object references of the constant
d = [0] * 23
print(d)
# EX:
s = [[-1, +1]] * 5
# under the cover in order:
"""
1 - the two int objects containing values -1 and +1 are created in the inner list
2 - that list object is then contained in another outer list
3 - a copy of the outer list is then multiplied by 5 creating 5 duplicate references to the inner list object
4 - the temporary outer list is disposed and is left with copied list object reference
5 - this new data structure is now bound to the reference s
"""
print(s)
# when one of the objects are modified it modifies all the elements
# all contain the same object reference
s[3].append(7)
print(s)

# MORE ON LIST
# to find an element in a list use .index(item) method
# returns the index of an item input in method call and returns ValueError if not found
# use exception handlers to work around
# EX:
w = "the quick brown fox jumps over the lazy dog".split()
try:
    i = w.index("fo")
    print("found", w[i])
except ValueError:
    print("not found")
# use .count(item) to return the number of matching elements
# returns the number of matching elements specified in method call (0 if none are found)
print(w.count("the"))
print(w.count("cat"))
# to test for membership of not use:
# in = for membership
# not in = for no membership
print("dog" in w)
print("cat" not in w)
# elements can be removed from a list using the del keyword
# takes one parameter being a reference to the list element, list[index]
# removes it from the list shortening it, if elements are right of it they will have their indexes shift left
# EX:
print(w)
del w[3]
print(w)
# also possible to remove elements by value with the .remove(item) method
# if item is found it will be removed
# if not a ValueError will be raised
try:
    del w[w.index("jumps")]
    print("removed")
    print(w)
except ValueError:
    print("element not found")
# or
try:
    w.remove("cat")
    print("removed")
    print(w)
except ValueError:
    print("element not found")
# items can be inserted into a list with the .insert(index, item) method
# takes the index that the item would be inserted at and the item that will be inserted
# if items are to the right of or there is an item in place of where it is going to be inserted
# everything index of such is shift once to the right, index increased by 1
print(w)
w.insert(3, "cat")
w.insert(4, "ran")
w[0] = w[0].capitalize()
# this sentence can then be reformed with the .join space separator that will add a space in between each element
w = ' '.join(w) + "."
print(w)

# GROWING LISTS
# concatenating lists to a new list object does not modify any operands (the lists used to create new list)
# a new list is created when using concatenation
# EX:
m = [2, 4, 6]
n = [9, 7, 4]
k = m + n
print(k)
# while the augmented assignment operator or .extend() changes the assignee in place
# an existing list is modified
k += [8, 1]
print(k)
# can also use .extend() to extend onto a list of elements specified in method call
k.extend([5, 3])
print(k)

# REVERSING AND SORTING LISTS
# a list can be reversed in place with the .reverse() method
# EX:
g = [1, 11, 21, 1211, 112111]
g.reverse()
print(g)
# a list can ber sorted in place using the .sort() method
# if nothing is input into method call it will go from smallest to largest
# EX:
d = [5, 17, 41, 29, 71, 149, 3299, 7, 13, 67]
d.sort()
print(d)
# the .sort() method call accepts two optional arguments, key and reverse
# if reverse=True, reverse is set to true and it is now largest to smallest
d.sort(reverse=True)
print(d)
# the key argument accepts a function and produces an object sort key for item which will then dictate sorting order
"""
for example the built in len() function can be used to order based on length
"""
# EX:
h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
# to use a function as a reference the method call argument header is not needed and just the name is
h.sort(key=len)
print(h)
# can then join these words back together to create a sentence
h = ' '.join(h) + "."
print(h)
# sometimes it is preferred to leave the original list unmodified
# sorted() and reversed() serve this purpose
# sorted() works the same as .sort() but instead returns a list to be assigned to a reference
# takes the list as an argument instead of being a method call of the list
# EX:
x = [4, 9, 2, 1, -3]
y = sorted(x, key=abs, reverse=True)
print(y, "\n", x)
# reversed is a function as well but instead returns an iterator
# to get a list, you must use the list constructor on the returned iterator value
# EX:
p = [6, 3, 9, 2]
q = reversed(p)
print(q)
q = list(q)
print(q)

# DICTIONARY
# unordered mapping from unique immutable keys to mutable values
# literals:
"""
delimited by { }
key-value pairs comma separated
corresponding keys and values joined by colon
keys are formatted like strings
"""
# EX:
urls = {'Google': "google.com",
        'Pluralsight': "pluralsight.com"}
# the values are accessible via the keys
print(urls['Pluralsight'])
# the keys must be unique within each dictionary, no repeat keys
# can have duplicate values but not keys
# under the cover/rules:
"""
the dict contains keys linked to the key argument (must be immutable), strings, numbers, tuples are fine, lists are not
it the links the value to the that specific value to the value argument (can be mutable), all mutable and not types
then the key and value are linked
never rely on order can be essentially random, and may even vary on different runs of same program
all stored within the dict
"""
# constructor dict() will convert other types to dictionary
# used with series of key-value pairs represented by tuples
# EX:
name_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28)]
name_and_ages = dict(name_and_ages)
print(name_and_ages)
# also able to create a dict with keyword arguments
# python will recognize the keyword reference as the key string and the value as the value
# with this method key-value pairs with tuples are not needed
# EX:
phonetic = dict(a='alfa', b='bravo', c='charlie')
print(phonetic)
phonetic = dict({'a': "alfa", 'b': 'bravo'})
print(phonetic)
# same with lists, dictionary coping is shallow
# this is because the values are still references to their objects
# there are two means of doing these shallow copies, .copy() and dict()
# first being .copy() method
# EX:
# see as the vales are input as hexadecimal but converted to decimal
d = dict(goldenrod=0xDAA520, indigo=0x4B0082, seashell=0xFFF5EE)
print(d)
e = d.copy()
print(e)
# or the dict() method
e = dict(d)
print(e)
# though since these are shallow copies, if any values are modified within the original, the copies will be modified
# if the dictionary needs to be expanded with other key-value pairs from another dict use .update()
# .update() extends the dict called upon with the dict input in method call
e.update(wheat=0xF5DEB3, khaki=0xF0E68C)
print(e)
# if the update method call contains a keys with same names as those within the dict being called upon
# the value of that pre-existing key will be updated to match the updated key
# the updated key values will replace duplicate key values
e.update(goldenrod=0xEBB703)
print(e)
# dict are iterable and key be used with for loops
# the key will be the item iterator
# the value can be obtained though calling the key on the dict, dict[key]
# the keys can be returned in a random order
# though this method is not commonly used because default iteration over dict are by key
for key in e:
    print(f"{key} = {e[key]}")
# or
for key in e.keys():
    print(f"{key} = {e[key]} 2")
# if we just want to iterate over the values, the .values() method can be used
# it returns a series of all values of dictionary so no keys are needed for values
# no real efficient way to get keys so it is only useful when keys are not needed
for value in e.values():
    print(value)
# when wanting to iterate over both easily, use .items() method
# returns the two key-value tuple pairs
# can then be unpacked into two separate references
for key, value in e.items():
    print(f"{key} = {value} 3")
# the membership operator in and not in work only on the keys
print('goldenrod' in e)
print(0xEBB703 in e)
# the del dict[key] can remove any key-value pair but works same as all other times
# the key must be used to find the item to be removed, value can not be used
try:
    del e['goldenrod']
    print("found")
    print(e)
except ValueError:
    print("not found")
# keys must be immutable
# values may be mutable
# EX:
m = {'H': [1, 2, 3],
     'He': [3, 4]}
print(m)
n = m.copy()
print(n)
# use augmented assignment to modify the 'H' key
# even though m was modified, since n contains the same mutable object reference, it carries the modification to 'H'
m['H'] += [4, 5, 6, 7]
print(n)
# the dictionary itself is mutable and a key value can be added just by making a new key equal a value
# simply assign a new key to a value and it is added to the dictionary
# dict are mutable
m['Li'] = [6, 7]
print(m)
# to increase readability, a standard library called pprint (pretty printing) can be used
# the "as pp" changes its reference name, assigning an object to a variable name
# if the function pprint wasn't rebound as pp, it would override the module name reference pprint
# poor design to have functions name same as module
# this function knows how to pretty print all built in data structures (dict, tuple, list...)
from pprint import pprint as pp
pp(m)
# the length, len(s), is determined by the number of keys
d = {'tst_one': "tst1", 'tst_two': "tst2"}
print(len(d))


# SET
# unordered collection of unique, immutable objects/elements
# the collection is mutable meaning elements can be added and removed from set
# but the elements are immutable, like keys of dict
# similar to dict
# under the cover/rules:
"""
delimited by { }
each item must be immutable
unlike dict pairs are not needed and each element alone must be immutable
single comma separated items
"""
# EX:
p = {6, 28, 496, 8128, 33550336}
print(p)
# empty {} create a dict
# so to create an empty set must refer to the set() constructor
# EX:
d = {}
print(type(d))
e = set()
print(type(e))
# the set() constructor accepts any iterable series of values, list, tuple
# any duplicates as discarded
# a use of set can be to remove any duplicates, not order preserving
s = set([2, 4, 16, 4096])
print(s)
# use case of removing duplicates
t = [1, 4, 2, 1, 7, 9, 9]
print(set(t))
# sets are iterable, though the order is useless and unenviable
# EX:
for x in s:
    print(x)
# membership is fundamental for sets
# in if in and not in if not in
# EX:
print(16 in s)
print(7 not in s)
# to add a single element to set, use .add(item) method
# the method call takes one parameter being the object that wants to be added to set
s.add(908)
# if adding a duplicate, its called for addition is silently ignored
# like dict, use .update(items) method to add multiple items to the set called upon
# works similar to dict as in it will extend the set with the new set values
s.update(set(t))
# or any iterable series
s.update([234, 9878])
print(s)
# removing elements from set work similar to dict, use .remove() or .discard()
# .remove(item) removes an item from set and returns KeyError if not
try:
    s.remove(234)
    print("found")
    print(s)
except KeyError:
    print("not found")
# .discard(item) removes item if found but still proceeds if not found, doesnt throw error
s.discard(9878)
print(s)
s.discard(9878)
# two copying methods: all copies are shallow
# .copy()
# set() constructor
# use .copy() the same as all collections
# call .copy() on original set
y = s.copy()
print(y)
# use set(series) constructor same as all other collections
# pass original set into constructor
z = set(s)
print(z)
# powerful parts of sets are the set algebra
# EX:
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}
# use s.union(s2) method that collects all data in both sets and combines
# commutative operation meaning order does not matter
# since sets delete duplicates, it returns every person and no two of same people
print(blue_eyes.union(blond_hair))
# order does not matter
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))
# to find all people with an attribute AND another attribute use s.intersection(s2)
print(blue_eyes.intersection(blond_hair))
# this is commutative as well
print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))
# to find people with an attribute but NOT another attribute use s.difference(s2)
print(blue_eyes.difference(blond_hair))
# not commutative
print(blue_eyes.difference(blond_hair) == blond_hair.difference(blue_eyes))
# to find people with one attribute OR another attribute use s.symmetric_difference(s2)
print(blue_eyes.symmetric_difference(blond_hair))
# this is commutative
print(blue_eyes.symmetric_difference(blond_hair) == blond_hair.symmetric_difference(blue_eyes))
# 3 predicate methods tell us about the sets:
# 1 - check if one set is apart of another set using s.issubset(s2), returns True or False
# 2 - to check if one set contains another set use s.issuperset(s2), returns True or False
# 3 - to test if two sets share not members use s.isdisjoint(s2),
# s.issubset(s2) - s being what is inside s2
print(smell_hcn.issubset(blue_eyes))
print(taste_ptc.issubset(blue_eyes))
# s.issuperset(s2) - s being what contains s2
print(taste_ptc.issuperset(smell_hcn))
print(blue_eyes.issuperset(taste_ptc))
# s.isdisjoint(s2) - s and s2 being compared if either contain one another's members
# doesn't have to contain all members, just 1
print(a_blood.isdisjoint(o_blood))
print(blond_hair.isdisjoint(ab_blood))
# EXPERIMENT WITH THIS CREATING DATA AND SUCH AT TESTING, AND A LITTLE WITH TUPLE UNPACKING

# COLLECTION PROTOCOLS
# a protocol is a type of operations a type must support in order to support that protocol
# support for protocol demands specific behavior from type
# all types seen support the container sized and iterable protocols
"""
protocol - implementing collections
# container must have membership testing, in and not in
container - str, list, range, tuple, bytes, set, dict
# sized must be able to determine number of elements, len(s)
sized - str, list, range, tuple, bytes, set, dict
# can produce an iterator with iter(s), yielding elements one-by-one while requested (used with for loops)
iterable - str, list, range, tuple, bytes, set, dict
# sequence requires items can be retrieved with seq[index], can find items with .index(item), 
  can count items with .count(item), and produce a reversed sequence with reversed(seq)
sequence - str, list, range, tuple, bytes
# only covered one of each - dive deeper later
mutable sequence - list
mutable set - set
mutable mapping - dict
"""

# TESTING
# experiment with this creating data and such at testing, and a little with tuple unpacking


def data_analytics(user):
    avg, ind = 0, 0
    for index, val in enumerate(user):
        avg += val
        ind = index
    avg = avg / ind
    user.sort()
    if len(user) % 2 != 0:
        mid = user[int(len(user) / 2)]
    else:
        median_plus = user[int(len(user) / 2 - 1)]
        median_minus = user[-int(len(user) / 2)]
        mid = (median_plus + median_minus) / 2
    single_set = set(user)
    counted = 0
    count = None
    for num in single_set:
        if user.count(num) > counted and user.count(num) > 1:
            counted = user.count(num)
            count = num
    return avg, mid, count


if __name__ == "__main__":
    mean, median, mode = data_analytics([2, 5, 9, 3, 10, 11, 12, 13, 239487, 213, 45543, 3])
    print(f"mean = {mean:.2f}, median = {median}, mode = {mode if mode is not None else 'NO-MODE'}")


# create venn diagram with set, figure something out to do it ab
# im tried now


def text_valid(string):
    user = input(f'Some may be: hair color, cuteness, prettiness, straight fingers, etc...\n{string}')
    user_set = set()
    while True:
        if user.lower() == "exit":
            return user_set
        if user.replace(" ", "").isalpha():
            user_set.add(user)
        user = input(f'{" " * (len(string) - 2)}: ')


def d_v_g():
    """
    could have used enumerate(ser, 1) to remove the -1 off the length comparisons and just have to -1 to set next list
    but was too far into program and don't want to spend too much time on
    """
    d_string = text_valid('Please input attributes for David (type "exit"): ')
    g_string = text_valid('Please input attributes for Grace (type "exit"): ')
    similarities = list(d_string.intersection(g_string))
    dif_d = list(d_string.difference(g_string))
    dif_g = list(g_string.difference(d_string))
    print(f"\n"
          f" David's Differences:         Similarities:         Grace's Differences:".replace("\t", " "))
    if similarities != [] and dif_d != [] and dif_g != []:
        for (d_i, d_v), (sm_i, sm_v), (g_i, g_v) in zip(enumerate(dif_d), enumerate(similarities), enumerate(dif_g)):
            print(f" -{d_v}{' ' * (28 - len(d_v))}-{sm_v}{' ' * (21 - len(sm_v))}-{g_v}")
            if sm_i == len(similarities) - 1 and d_i < len(dif_d) - 1 and g_i < len(dif_g) - 1:
                # no similarities - yes david - yes grace
                dif_dd = dif_d[d_i + 1:]
                dif_gg = dif_g[g_i + 1:]
                for(d_ii, d_vv), (g_ii, g_vv) in zip(enumerate(dif_dd), enumerate(dif_gg)):
                    print(f" -{d_vv}{' ' * (28 - len(d_vv))}{' ' * 22}-{g_vv}")
                    if d_ii == len(dif_dd) - 1 and g_ii < len(dif_gg) - 1:
                        # no similarities - no david - yes grace
                        dif_ggg = dif_gg[g_ii + 1:]
                        for g_vvv in dif_ggg:
                            print(f" {' ' * 51}-{g_vvv}")
                    elif d_ii < len(dif_dd) - 1 and g_ii == len(dif_gg) - 1:
                        # no similarities - yes david - no grace
                        dif_ddd = dif_dd[d_ii + 1:]
                        for d_vvv in dif_ddd:
                            print(f" -{d_vvv}")
            elif sm_i < len(similarities) - 1 and d_i == len(dif_d) - 1 and g_i < len(dif_g) - 1:
                # yes similarities - no david - yes grace
                similarities_ = similarities[sm_i + 1:]
                dif_gg = dif_g[g_i + 1:]
                for (sm_ii, sm_vv), (g_ii, g_vv) in zip(enumerate(similarities_), enumerate(dif_gg)):
                    print(f" {' ' * 29}-{sm_vv}{' ' * (21 - len(sm_vv))}-{g_vv}")
                    if sm_ii == len(similarities_) - 1 and g_ii < len(dif_gg) - 1:
                        # no similarities - no david - yes grace
                        dif_ggg = dif_gg[g_ii + 1:]
                        for g_vvv in dif_ggg:
                            print(f" {' ' * 51}-{g_vvv}")
                    elif sm_ii < len(similarities_) - 1 and g_ii == len(dif_gg) - 1:
                        # yes similarities - no david - no grace
                        similarities__ = similarities_[sm_ii + 1:]
                        for sm_vvv in similarities__:
                            print(f" {' ' * 29}-{sm_vvv}")
            elif sm_i < len(similarities) - 1 and d_i < len(dif_d) - 1 and g_i == len(dif_g) - 1:
                # yes similarities - yes david - no grace
                similarities_ = similarities[sm_i + 1:]
                dif_dd = dif_d[d_i + 1:]
                for (sm_ii, sm_vv), (d_ii, d_vv) in zip(enumerate(similarities_), enumerate(dif_dd)):
                    print(f" -{d_vv}{' ' * (28 - len(d_vv))}-{sm_vv}")
                    if sm_ii == len(similarities_) - 1 and d_ii < len(dif_dd) - 1:
                        # no similarities - yes david - no grace
                        dif_ddd = dif_dd[d_ii + 1:]
                        for d_vvv in dif_ddd:
                            print(f" -{d_vvv}")
                    elif sm_ii < len(similarities_) - 1 and d_ii == len(dif_dd) - 1:
                        # yes similarities - no david - no grace
                        similarities__ = similarities_[sm_ii + 1:]
                        for sm_vvv in similarities__:
                            print(f" {' ' * 29}-{sm_vvv}")
            elif sm_i == len(similarities) - 1 and d_i == len(dif_d) - 1 and g_i < len(dif_g) - 1:
                # no similarities - no david - yes grace
                dif_gg = dif_g[g_i + 1:]
                for g_vv in dif_gg:
                    print(f" {' ' * 51}-{g_vv}")
            elif sm_i < len(similarities) - 1 and d_i == len(dif_d) - 1 and g_i == len(dif_g) - 1:
                # yes similarities - no david - no grace
                similarities_ = similarities[sm_i + 1:]
                for sm_vv in similarities_:
                    print(f" {' ' * 29}-{sm_vv}")
            elif sm_i == len(similarities) - 1 and d_i < len(dif_d) - 1 and g_i == len(dif_g) - 1:
                # no similarities - yes david - no grace
                dif_dd = dif_d[d_i + 1:]
                for d_vv in dif_dd:
                    print(f" -{d_vv}")
    elif similarities != [] and dif_d == [] and dif_g != []:
        # yes similarities - no david - yes grace
        for (sm_i, sm_v), (g_i, g_v) in zip(enumerate(similarities), enumerate(dif_g)):
            print(f" {' ' * 29}-{sm_v}{' ' * (21 - len(sm_v))}-{g_v}")
            if sm_i == len(similarities) - 1 and g_i < len(dif_g) - 1:
                # no similarities - no david - yes grace
                dif_gg = dif_g[g_i + 1:]
                for g_vv in dif_gg:
                    print(f" {' ' * 51}-{g_vv}")
            elif sm_i < len(similarities) - 1 and g_i == len(dif_g) - 1:
                # yes similarities - no david - no grace
                similarities_ = similarities[sm_i + 1:]
                for sm_vv in similarities_:
                    print(f" {' ' * 29}-{sm_vv}")
    elif similarities == [] and dif_d != [] and dif_g != []:
        # no similarities - yes david - yes grace
        for (d_i, d_v), (g_i, g_v) in zip(enumerate(dif_d), enumerate(dif_g)):
            print(f" -{d_v}{' ' * (28 - len(d_v))}{' ' * 22}-{g_v}")
            if d_i == len(dif_d) - 1 and g_i < len(dif_g) - 1:
                # no similarities - no david - yes grace
                dif_gg = dif_g[g_i + 1:]
                for g_vv in dif_gg:
                    print(f" {' ' * 51}-{g_vv}")
            elif d_i < len(dif_d) - 1 and g_i == len(dif_g) - 1:
                # no similarities - yes david - no grace
                dif_dd = dif_d[d_i + 1:]
                for d_vv in dif_dd:
                    print(f" -{d_vv}")
    elif similarities != [] and dif_d != [] and dif_g == []:
        # yes similarities - yes david - no grace
        for (sm_i, sm_v), (d_i, d_v) in zip(enumerate(similarities), enumerate(dif_d)):
            print(f" -{d_v}{' ' * (28 - len(d_v))}-{sm_v}")
            if sm_i == len(similarities) - 1 and d_i < len(dif_d) - 1:
                # no similarities - yes david - no grace
                dif_dd = dif_d[d_i + 1:]
                for d_vv in dif_dd:
                    print(f" -{d_vv}")
            elif sm_i < len(similarities) - 1 and d_i == len(dif_d) - 1:
                # yes similarities - no david - no grace
                similarities_ = similarities[sm_i + 1:]
                for sm_vv in similarities_:
                    print(f" {' ' * 29}-{sm_vv}")
    elif similarities != [] and dif_d == [] and dif_g == []:
        # yes similarities - no david - no grace
        for sm_v in similarities:
            print(f" {' ' * 29}-{sm_v}")
    elif similarities == [] and dif_d != [] and dif_g == []:
        # no similarities - yes david - no grace
        for d_v in dif_d:
            print(f" -{d_v}")
    elif similarities == [] and dif_d == [] and dif_g != []:
        # no similarities - no david - yes grace
        for g_v in dif_g:
            print(f" {' ' * 51}-{g_v}")


if __name__ == "__main__":
    print("")
    mean, median, mode = data_analytics([2, 5, 9, 3, 10, 11, 12, 13, 239487, 213, 45543])
    print(f"mean = {mean:.2f}, median = {median}, mode = {mode if mode is not None else 'NO-MODE'}")
    print("")
    d_v_g()


"""
                                               : brown hair
                                               : not cute
                                               : not straight fingers
                                               : not pretty
                                               : exit
"""
