# INTRO
# str - byte - list - dict - for loops(intro)

# STRINGS
# immutable sequences of unicode codepoints
# can use " or '
# can have either in each othe " '' " or ' "" '
print("string")
print('"string"')
# multi-line strings
# triple single or double quotes and each enter is the next line """ or '''
print("""this1 
is1
multi1""")
# can also use "\n" - universal newline support
print("this2\nis2\nmulti2")
# \t allows tabs in a string
print("\ttab spaces")
# \" or \' for the quote characters in a string
print(" \" the quotes \' ")
# \\ to place a backslash in a string
print("\\ backslash")
# raw strings don't support any escape sequences
# call it by using r'<string>'
print(r'C:\Users\David\pythons')
# use str() to create strings of any types
print(str(4))
print(str(-.03492))
# sequence types
# calling certain characters of string, called through brackets and 0 base index
# the returned is a single character string, no character type
seq_test = "testing"
print(seq_test[2])
# use type() to determine type of value
print(type(seq_test[2]))
print(type(4.029))
# to find more about strings
# help() in repl and input str - help(str)
# use capitalize() to capitalize first character and rest be lower
example1 = "daVid"
print(example1.capitalize())
# split splits the string up into a list at what is passed as a string argument
# if nothing is passed it will be whitespace
# returns a list of string objects
string_test = "this, is, a, string1"
print(string_test.split(", "))
# python is unicode based
# can input other language characters or use unicode numbers with \u<unicode>

# BYTES
# immutable sequences of bytes
# used for raw binary data and fixed with single byte character encoding such as ASCII
# the literal form is b' ' or b" "
# supports most of same operations as strings
# using split returns a list of byte objects
byte_test1 = b"this is a byte1"
print(byte_test1.split())
# can encode and decode using strings of certain unicode characters
# take the string, for example:
# -- string_en = " weird unicode characters "
# -- byte_en = string_en.encode('utf-8')
# -- byte_en = b" \xc3\xa5 ... "
# the byte_en will now be a byte object will th encoded unicode values
# so instead of the values it will be represent as the code, \xc3\xa5
# then to decode it back to a string use
# -- byte_en = b" \xc3\xa5 ... "
# -- string_en = byte_en.decode('utf-8')
# -- string_en = " weird unicode characters "
# the string_en will now be a string object holding the characters and not the values of

# LISTS
# mutable sequences of objects
# list literal [x, y, z]
# 0 based index
list1 = [1, 2, 3]
print(list1[0])
# heterogeneous meaning it can have multiple types
# best practice to just have one
list2 = [1, "two", 3.03]
# [] empty list and use append to add to the end of it
list3 = []
list3.append(1.92748)
list3.append(2.39482)
print(list3)
# use list constructor to make a list of every character in a string, including spaces
print(list(" characters "))
# can also use white space
# if brackets aren't closed can keep going to next line
# can use a , after last object
list4 = ["one",
         "two",
         "three", ]

# DICT
# mutable mappings of keys to values
# keys and values
# key is followed by : with the value then separated by next key value pair with a ,
# {k1: v1, k2: v2}
dict1 = {"dict10": 10, "dict_greet": "greet"}
print(dict1["dict10"])
# if assign to a key that has not been added it will add it
dict1["dict1_name"] = "Dict"
print(dict1["dict1_name"])
# empty dicts are created with just {}
dict2 = {}

# FOR-LOOPS
# visit each item in an iterable series
# syntax:
# for _item_ in _iterable_:
#   ... body ...
for1 = ["Item1", "iTem2", "itEm3", "iteM4"]
for item in for1:
    print(item)
# when iterating over a dictionary you get the keys
# then be used in body to get the values
for2 = {"key_one": "value1", "key1.0": 1.001, "key1": 1}
for key in for2:
    # print function can accept multiple arguments
    print(key, ":", for2[key])
# to exit python repl use "ctrl + z" on windows and "ctrl + d" on linux

# TOGETHER
# imports text data
from urllib.request import urlopen
# using a with statement with external objects helps with resource leaks
with urlopen("http://sixty-north.com/c/t.txt") as story:
    story_words = []
    # goes through each line of story and then splits words based off whitespace
    for line in story:
        line_words = line.split()
        # takes the list of split words and goes through it adding each word to story_words list
        for words in line_words:
            story_words.append(words)
# got a list of byte objects
print(story_words)
with urlopen("http://sixty-north.com/c/t.txt") as story:
    story_words = []
    # decodes the words just before they are added so they are added as strings
    # added to the split line to save variable space
    for line in story:
        line_words = line.decode("utf-8").split()
        for words in line_words:
            story_words.append(line_words)
# prints a list of string objects
print(story_words)

# TESTING
bus = [{"row": 1, "seat": [1, 2, 3]},
       {"row": 2, "seat": [1, 2, 3]},
       {"row": 3, "seat": [1]},
       {"row": 4, "seat": [1, 2]},
       {"row": 5, "seat": [1, 2, 3, 4]},
       {"row": 6, "seat": [1, 2, 3, 4]},
       {"row": 7, "seat": [1]},
       {"row": 8, "seat": [1, 2, 3, 4]},
       {"row": 9, "seat": [1, 2, 3, 4]}]


def seating():
    flag = True
    while flag:
        while True:
            bus_options = get_string("Would you like to find or remove seats: FIND, REMOVE, or EXIT ")
            if bus_options.upper() == "FIND":
                break
            elif bus_options.upper() == "REMOVE":
                name = get_string("What is the name in your seat: ")
                found = False
                for i in bus:
                    k = 0
                    for seat in i["seat"]:
                        k += 1
                        if seat == name.capitalize():
                            print("The seat with name {0} in row {1}, seat {2}, will now be removed."
                                  .format(seat, i["row"], k))
                            i["seat"][k - 1] = k
                            found = True
                            break
                    if found:
                        break
                if not found:
                    print("The seat with name {0} could not be found.".format(name.capitalize()))
            elif bus_options.upper() == "EXIT":
                return
        while True:
            open_seats = 0
            for i in bus:
                for seat in i["seat"]:
                    if user_get_elements(seat, i["seat"]):
                        open_seats += 1
            if open_seats == 0:
                print("The bus is full.")
                flag = False
                break
            print("*enter a 0 to exit the selection process*")
            select_exit = False
            while True:
                row_in = data_valid("What row do you want: ") - 1
                if get_elements(row_in, bus):
                    break
                elif row_in == -1:
                    select_exit = True
                    break
            if select_exit:
                break
            row = bus[row_in]["seat"]
            open_seats = 0
            print("Now accessing row {0}.".format(bus[row_in]["row"]))
            for seat in row:
                if user_get_elements(seat, row):
                    print("Seat number {0} is open.".format(seat))
                    open_seats += 1
                else:
                    print("This seat is taken by {0}.".format(seat))
            if open_seats > 0:
                while True:
                    while True:
                        sitting = data_valid("What of the open seats do you want: ") - 1
                        if get_elements(sitting, row):
                            break
                    if user_get_elements(row[sitting], row):
                        row[sitting] = get_string("What is your name: ").capitalize()
                        break
                break
            else:
                print("The row is full. Sorry pick another one.")


def data_valid(text):
    while True:
        x = input(text)
        if x.isdigit():
            return int(x)


def get_string(text):
    while True:
        y = input(text)
        if y.isalpha():
            return y


def get_elements(sw, rwo):
    y = 0
    while y < len(rwo):
        if sw == y:
            return True
        y += 1
    return False


def user_get_elements(uw, rwo):
    y = 1
    while y <= len(rwo):
        if uw == y:
            return True
        y += 1
    return False


# this entire program simulates a booking agency for buses
# this could be used to assign and remove people to and from a bus
# the code is flexible meaning it changes with the buses features
# WILL REMAKE THIS WITH CLASSES

seating()
print(bus)
