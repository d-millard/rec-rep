# just some testing
print("Hello world!!!!")
x = 2
y = 2
z = "hello"
print(z + " " + str(x + y) + ".")

x = "if x == y && z == \"hello\":"

# shows a list and how to add items to beginning
list = []
list.append(1)
list.append(2)
list.append(3)
print(list[2])

# shows setting the length of a list
listLimit = [6, 90, 9, 2, 4, 4, 8]
print(len(listLimit))
# or
print(listLimit.__len__())

# shows adding list items when list is created
numbers = [1, 2, 3, 4, 5]
print(numbers[0])

squared = 7 ** 2

repeatedString = "hello " * 10
print(repeatedString)

listAddition1 = [1, 2, 3]
listAddition2 = [5, 6, 7]
listAddition3 = listAddition1 + listAddition2
print(listAddition3)

# formatting prints
# %s format strings
# %d format integers
# %f floating point numbers
# %.<number of digits>f floating point numbers with fixed decimals places (don't need <>)
# %x/%X integers in hex representation (lowercase/uppercase)
formatStrings = "david"
formatStrings2 = 30.97452
print("hello %s and %.3f" % (formatStrings, formatStrings2))


# type hinting
# help add data types
# python has trouble detecting data types but this doesnt really help just data validate
def add_numbers(a : int, b: int) -> int:
    return a + b


print(add_numbers(5, 6))

# types don't need to be declared
# Integers and floats
# allows adding ints and floats seamlessly
inty = 10
pi = 2.14159 + inty
print(int(pi) == 12)
print(float(inty) == 10.0)

# strings can be ' ' or " " or """ """ - ( tripe quotes usually function or class documentation)
print('Hey' == "Hey" == """Hey""")
# treated like comment
"""
this is 
multi line
comment
"""
print("See")

# methods
"hello".capitalize()  # = Hello not all caps
"hello".replace("e", "a")  # = hallo
"hello".isalpha()  # True if all characters are letters
"123".isdigit()  # True useful when converting to int
"some,csv,value".split(",")  # makes a list of every term between , so ["some", "csv", "values"]

# FORMAT method
name = "py"
machine = "hal"
print("Nice to meet you {0} I am {1}".format(name, machine))
# or
print(f"Nice to meet you {name} I am {machine}")

# boolean
# capital first letter - True or False
print(int(True) == 1)
print(int(False) == 0)
print(str(True) == "True")
# None is similar to null
placeholder = None

# if statements
number = 6
if number == 5:
    print("is")
else:
    print("not")
# truthy values
number = 5
# if it is integer
if number:
    print("is Truthy1")
text = "Python"
# if it isnt an empty string
if text:
    print("is Truthy2")
# if it is true
# if false will not execute
placeholder = True
if placeholder:
    print("is Truthy3")
# if none it will not execute
placeholder = None
if placeholder:
    print("is not Truthy4")
# not if statements
number = 5
if number != 5:
    print("Won't execute1")
# or not
# only true if falsy
placeholder = True
if not placeholder:
    print("Won't execute2")
# and conditions
# and - same as &&
# or - same as ||
if number == 5 and placeholder:
    print("and operator")
if placeholder or number == 6:
    print("or operator")
# ternary if statement
a = 1
b = 2
print("bigger" if a > b else "smaller")

# LISTS
# functions similar to arrays
student_test = []  # empty list
student = ["mark", "katrina", "jessica"]
print(student[0])
print(student[2])
print(student[-1])  # last element in list
student[0] = "james"  # reassign the first element
# append function
# add to end
student.append("homer")
# use in operator to check if element is within list
if "james" in student:
    print("theyre in here")
# how to get length of list
# use len(<list>)
print(len(student) == 4)
# multiple types in lists can occur, int, float, string
mult = [1, 9.86, "string"]
# best if one type a list
# del removes an element form list
# list shifts to left
del student[2]
# now student = [ "james", "katrina", "homer"]
if student[2] == "homer":
    print("reassignment")
# slicing
# starts if first number input and ends with second
# [x:y] or [x:-y]
print(student[1:])
print(student[1:-1])

# LOOPS
student_names = ["james", "katrina", "homer"]
# name serves as reference to each element
for i in student_names:
    print(f"Student name is {i}.")
# creates a list of the number of iterations that can be done
# set range in different ways
# uses indexes not actual length
x = 0
for index in range(10):
    x += 10
    print("value of x is {0}".format(x))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# start and stop point of range
x = 0
for index in range(5, 10):
    x += 20
    print("value of x is {0}".format(x))  # [5, 6, 7, 8, 9]
# increment with range function
x = 0
for index in range(5, 10, 2):
    x += 30
    print("value of x is {0}".format(x))  # [5, 7, 9]

# BREAK AND CONTINUE
# break stops the loop entirely
student_names = ["james", "katrina", "homer", "mark", "jake", "jerry"]
for i in student_names:
    if i == "mark":
        print("Found him!!!! " + i)
        break
    print("trying " + i)
# continue sends the loop to next iteration
for i in student_names:
    if i == "homer":
        continue
    print("trying " + i)

# WHILE
# works essentially the same as other while loops
x = 0
while x < 10:
    if not x == 7:
        print("{0} does not equal 7".format(x))
    print("count is {0}".format(x))
    x += 1

# DICTIONARY
# stores keys and values for certain objects
student = {
    "name": "Mark",
    "ID": 15163,
    "feedback": None
}
# list of dictionaries
all_students = [
    {"name": "Mark", "ID": 15163, "feedback": None},
    {"name": "katrina", "ID": 63112, "feedback": None},
    {"name": "jessica", "ID": 30021, "feedback": None}
]
# getting data in dictionaries is kind of like indexes
# put the key in [], [<key>]
print(student["name"])
# get function sets the first to try to find key of and second to say if first not found
print(student.get("last_name", "Unknown"))
# keys method outputs all the keys
print(student.keys())
# values method outputs all values corresponding to keys
print(student.values())
# uses some parallels as list
del student["name"]
# can add a key by putting a new key name in with a value
for k in all_students:
    k["new"] = None
# list of dictionaries can have unequal keys
all_students[0]["new2"] = "unequal"

# TEST
students = [
    {"name": "Mark", "ID": 15163, "feedback": None},
    {"name": "Jessica", "ID": 30021, "feedback": "It was ok"},
    {"name": "Katrina", "ID": 63112, "feedback": None}
]
for i in students:
    if i["feedback"]:
        print("100% {0}".format(i["feedback"]))
        continue
    print("the keys are {0}. The name is {1}, ID being {2}, and gave {3} feedback"
          .format(i.keys(), i["name"], i["ID"], i["feedback"]))
# or
for i in students:
    if i["feedback"]:
        print("100% {0}2".format(i["feedback"]))
    else:
        print("the keys are {0}. The name is {1}, ID being {2}, and gave {3} feedback2"
              .format(i.keys(), i["name"], i["ID"], i["feedback"]))

# TEST PARALLEL LISTS
l_one = ["make", "a", "new", "list"]
l_two = ["i", "am", "here", "another", "should", "turn"]
l_three = ["this", "is", "three", "now"]
l_four = ["werid"]


# function that copies one list to other smaller one, if both the same let user pick which one to copy
def copy_list(l_o, l_t):
    if len(l_o) > len(l_t) or len(l_o) == len(l_t):
        x = l_o
        y = l_t
        flag = True
    else:
        x = l_t
        y = l_o
        flag = False
    ind = 0
    while ind < len(y):
        y[ind] = x[ind]
        ind += 1
    if len(y) == len(x):
        if flag:
            print(y)
            print("Checkpoint 1.")
            return y
    ind2 = len(y) - len(x)
    while ind2 < 0:
        y.append(x[ind2])
        ind2 += 1
    print(y)
    print("Checkpoint 2.")
    return y


def check(c1, c2):
    if c1 == c2:
        return True
    return False


l_four = copy_list(l_three, l_four)
print(l_four)
print("the two lists are {0}".format(check(copy_list(l_one, l_two), l_one)))
print(".......")

# EXCEPTIONS
# try and except blocks of code
student = {
    "name": "Mark",
    "ID": 15163,
    "feedback": None
}
# KeyError is a error thrown if looking for a non-existent key in a dictionary
# works for any errors
# try first and except is error is thrown
# doesnt stop whole program
try:
    last_name = student["last_name"]
except KeyError:
    print("Error finding last_name")
# TypeError - example when adding int to string
student["last_name"] = "kowalski"
try:
    print(student.keys())
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:  # specify error and output it
    print("Error adding number to last name")
    print(error)  # output the error
except Exception:  # broad general exception handler, not preferred
    print("Unknown error")

# OTHER DATA TYPES
# complex - complex numbers
# bytes - series of ints ranging from 256
# bytearray similar to bytes
# tuple similar to lists but cannot change value
# set and frozenset
# only have uniqe objects
set([3, 2, 3, 1, 5]) == (1, 2, 3, 5)

# FUNCTIONS
# def keyword to indicate function
# followed by name and then by () with possible parameters, ending with colon
# return works same ways
# - STUDENT APP
students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        # to add an element to list in loop of another list just set equal
        students_titlecase = student["name"].title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332):
    # make a dictionary and add to students list
    student = {"name": name, "student_id": student_id}
    students.append(student)


student_list = get_students_titlecase()

# get input
# student_name = input("Enter student name ")
# student_id = input("Enter student ID ")

# add_student(student_name, student_id)
# print_students_titlecase()

# ARGUMENTS
# *args is variable arguments - takes any number of arguments
# don't use * when referring to it in body
# **kwargs is key word arguments - passes arguments over like a dictionary


def var_args(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])


# for variable arguments data is input like "is", 1, "insane", True, "."
# for keyword arguments data comes like named arguments and are treated somewhat like a dictionary
var_args("this", description="keyword arg ", feedback=None, pluralsight_subscriber=True)


# using the = 332 is the default parameter value if the user doesn't input a student_id parameter
def add_student(name, student_id=332):
    # make a dictionary and add to students list
    student = {"name": name, "student_id": student_id}
    students.append(student)


# named arguments allow the arguments to be called and specify which is which argument
add_student(name="Mark", student_id=15)  # 15 overrides the default of 332

# TEST
# ask user if they want to add user, when no is answer output the list
student_list_hw = []


# if user choses yes get valid name and id and add to list, send true if keep going or false if not
def ask_students(val):
    if val == "Y":
        name_hw = input("Please enter the student's name: ")
        while not name_hw.isalpha():
            name_hw = input("Please enter the student's name: ")
        id_hw = input("Please enter the student's ID: ")
        while not id_hw.isdigit():
            id_hw = input("Please enter the student's ID: ")
        add_hw(name_hw, id_hw)
        return True
    return False


# add the dict object to the list
def add_hw(name_h, id_h):
    dict_h = {"name": name_h, "ID": id_h}
    student_list_hw.append(dict_h)


# get input from user to determine if going or not, then when over output all of the list elements' properties
def display_out():
    flag = True
    while flag:
        go = input("Input a student? Y or N")
        go = go.upper()
        if go == "N" or go == "Y":
            flag = ask_students(go)

    for i in student_list_hw:
        print("{0}: {1}".format(i["name"].lower().capitalize(), i["ID"]))


# call the beginning function
# display_out()

# NESTING FUNCTIONS AND CLOSURES
# you can nest a function within another function
# use this in cases where you only want a function used within the outer function
# the inner function has access to outer functions variables
# the access of this variable is called a closure
def get_tes():
    def get_tes1():
        print("nest functions test")
    get_tes1()


get_tes()

# FILES - OPEN R/W
# student app
students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        # to add an element to list in loop of another list just set equal
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    # make a dictionary and add to students list
    student = {"name": name, "student_id": student_id}
    students.append(student)

# opens a file named students.txt, with access mode "a" meaning appending to file
# if want to add text to new file or opened file use a - append mode
# if you open a file in w - write mode it will overwrite anything on file
# .write function which will take a string and write to file, "\n" makes new lines
# use .close to close file and prevent any memory leaks
def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


# opening file in r - read mode
# .readlines function will call every line in file and create a list out of them (useful with for loops)
# call add student for each element in the .readlines list
def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


# throws exception because r needs file to exist but since using a handler code keeps running
read_file()
print_students_titlecase()
# get input
#student_name = input("Enter student name ")
#student_id = input("Enter student ID ")

#add_student(student_name, student_id)
#save_file(student_name)

# YIELD
# creates a generator function
students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


# goes through file and yields a single file
# iterates over file f
# during every iteration it yields a single line form file
"""
keeps sending back each line every time the caller need 
something and since yield doesnt stop the function it is in
a somewhat standby mode on the next iteration waiting for 
callers request
"""


def read_students(f):
    for line in f:
        yield line


read_file()
print()

# MORE ON YIELD / GENERATORS
# infinite square generator


def next_sqr():
    ok = 1
    # the while True creates an infinite generator
    # want generator to keep going until outside caller doesnt need it anymore
    while True:
        yield ok * ok
        ok += 1


for op in next_sqr():
    if op > 1000:
        break
    print(op)

# LAMBDA FUNCTIONS
# dont have name or def keyword
# short, can take arguments, and anonymous


# regular function
def double1(x1):
    return x1 * 2

# in comparison

# lambda function
# agruments go after the keyword "lambda" followed by the body


double2 = lambda x1: x1 * 2

# both are called the same
print(double1(5) == 10)
print(double2(5) == 10)

# useful in higher-order function which take another function as argument

# CLASSES
# class keyword followed by name
# ex. "class Test:"
# instances
# ex. "test = Test()"
# special methods like constructor
# ex. "test1 = Test("testing")"

# DEFINING CLASSES
# ADDING METHODS TO CLASS
# CONSTRUCTOR AND OTHER SPECIAL METHODS
# INSTANCE AND ATTRIBUTES
students = []


class Student:
    # class attributes
    # tend to be static and standard across all instances
    school_name = "Springfield"
    # constructor method
    # uses __init__

    def __init__(self, name, student_id=332):
        # variables set with the self are available throughout the entire instance
        self.name = name
        self.student_id = student_id
        students.append(self)
    # self refers to instance of class
    # way refereed to class from class
    # used when calling methods/variables in class

    # string method
    # changes the output of print() reference
    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    # even though the school_name is static across all instances it still required self. to be called
    def get_school_name(self):
        return self.school_name

    # dont use this method adds to a list instead of making attributes of instance
    def add_student(self, name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)
        # recursion could be
        # self.add_student()


jake = Student("Jake")
print(jake)
# class attribute so doesn't need instance to call
print(Student.school_name)

# INHERITANCE AND POLYMORPHISM
# to inherit form another class use other classes as parameters in class name's header
# HighSchoolStudent is derived form the parent class Student
# not access modifiers so no public, private, or protected


class HighSchoolStudent(Student):
    # override the class attribute of Student
    school_name = "Springfield HighSchool"

    def get_school_name(self):
        return "This is a high school student " + self.school_name

    def get_name_capitalize(self):
        # super() keyword gets a method or varible form parent class Student
        original_value = super().get_name_capitalize()
        return original_value + "-HS"


james = HighSchoolStudent("james")
# shows how HighSchoolStudent has access to Student methods
print(james.get_school_name())
print(james.get_name_capitalize())

# BREAKING APP INTO MODULES

# CREATING VIRTUAL ENVIRONMENTS
# pip install virtualenv
# create the environments with "virtual env_name"
# specify python type with "virtualenv --python=python2.7 env_name"
# to go into the virtual environment type "env_name\Scripts\activate" (only for windows)
# to go out type "deactivate"
# if packages are installed in the env it will only be inside it

# DEBUGGING PYTHON CODE
# breakpoint, when reached will pause the environment and allow you to inspect so far
print("The red dot is the breakpoint")
# when running debugger mode it will stop execution as soon as breakpoint is reached
# has options like stepping into over and back to determine other issues
# will step into libraries if needed

# CREATING AN EXECUTABLE FILE
# use a package called "pyinstaller" that converts your code to .exe

# CREATING A SETUP WIZARD
# download "inno setup"
# use script wizard because its way easier
# compiler settings
# select dist file as ouput base file

