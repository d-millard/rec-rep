# INTRO
# importing and using modules

# CREATING, RUNNING, AND IMPORTING MODULE
# a file created in a python working file in c drive
# must change directories till Python_Fundamentals
# then type file want to run
# and prints will be displayed
print("go to word 'story_example_one'")

# DEFINING FUNCTIONS AND RETURNING VALUES
# use "def" keyword followed by name, parameters and a colon
# then use the return keyword to stop the function fully and return a value
# then called using the name and any arguments needed


def square(x):
    return x * x


print(square(9))
# you can stop a function early with a return keyword with nothing following it
# stops function and returns nothing
# this actually returns None


def even_or_odd(n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")


even_or_odd(12)
# the function returns None
return_None = even_or_odd(9)
print(return_None)

# DISTINGUISHING BETWEEN MODULE IMPORT AND MODULE EXECUTION
# changes up the "story_example_one" to include functions
# special attributes in python are defined by double underscores
# one example being:
# __name__
# gives the means to run as script of imported to REPL
# to test this use story example based in the python work learning folder with command line
# works same as calling function but used in the cmd line to automatically run like a script
# useful in importing into repl and running as script, to determine if run as a script or imported into another module
# to determine __name__ must return a value of "__main__"
# only really useful in repl
# used only when the the file is being directly ran, not run on something imported into another module

# PYTHON EXECUTION MODEL
# when function definitions and other import executions occur when module is imported or executed
# code within function are bound to name of function
# a python module == convenient import with API
# a python script == convenient execution from command line
# a python program == many modules
# make python code in module and scripts for easy access through python repl through the use of if _name__ == "__main__"

# MAIN FUNCTIONS AND COMMAND LINE ARGUMENTS
# main() function -- doest actually have to be called this
# adding these functions to story_example_one
# allows for all imports to occur within and then all executes to occur once called
# works as the executable flow controller calling everything when needed in order
# when importing in repl, select functions can be done with:
# from story_example_one import (fetch_words, print_words)
# or to import everything:
# from story_example_one import *
# not recommended in most cases other than casual because it can wreak havoc with no control over what is imported
# in this case in repl, print_words function isn't working as intended because it can print anything entered
# works for strings:
print(f"""print_words(\"Strings are iterable too\")
S
t
r
i
n
g
s
       
a
r
e
 
i
t
e
r
a
b
l
e
       
t
o
o""")
# refactor the print_words function easily with shift+F6 to rename everything with same name
# replace hard coded url with flexible variable that can be accessed as a command line argument
# use sys (an import) and argv (determines the command line argument it will get from) as show in story_example_one
# when running a python file in command line first is the name (story_example_one.py) followed by second argument (url)
# EX: $python3 story_example_one.py http://sixty-north.com/c/t.txt
# this argument is kind of created as a variable and can be called on at any time
# some advanced command line argument parsing could be:
# a python standard library: argparse
# many third-party options like docopt

# DOCUMENTING CODE USING DOCSTRINGS
# use docstrings to document code in python code
# start it with """ and finish with """
"""
This is an example
returns nothing
"""
# three conventions are used
# 1 - pep 257 - not widely adopted
# 2 - reStructuredText / Sphinx - html documentation
# 3 - google python style guide - preferred with being machine parsed while still readable at console
# FORMAT EX:
"""Fetch a list of words from URL

Args:
    url: The URL of an UTF-8 text document.
Returns:
    A list of strings containing words
    of a story.
"""
# these docstrings can then be accessed through help through the repl with help
# after imports type help(<function>)
# EX:
# input - help(fetch_words)
print(f"""Fetch a list of words from URL

    Args:
        url: The URL of an UTF-8 text document.
    Returns:
        A list of strings containing words
        of a story.
    """)
# module docstrings are placed at beginning of module before any statements
# when requesting help one whole module get all useful information - the module description and docstring of functions

# DOCUMENTING CODE WITH COMMENTS
# begin with a hash symbol and continue to end of line
print("not comment")  # print("is a comment")

# SHEBANG
# used a lot on unix based systems
# at the top of program begins with a hash followed by exclamation mark
# allows program loader to identify which interpreter should be used to run the program
# then a path is specified and python version that is being ran
# typical python3 ends in env and can work with other virtual environments
# EX:
"""
#!/usr/bin/env python3
"""
# on widows shebangs can ve used to make .exe


# TESTING
# working with module and cmd line
# find test module as testing_one.py, found in (Module 3 and fundamentals folder)
