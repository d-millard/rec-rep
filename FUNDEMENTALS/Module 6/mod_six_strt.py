# INTRODUCTION
"""
exception handling is a mechanism for stopping "normal"
program flow and continuing at some surrounding context of code block
"""
# stopping flow with with signal, then continuing on other block of code
# exceptions: key concepts
"""
raise exception - to interrupt program flow (the exception being thrown)
handle exception - resume control (have a handler ready for specific exception raise)
unhandled exceptions - will terminate the program (like index out of range, wacky stuff)
exception objects - contain information about the exceptional even (data of exception)
"""
# exceptionally is a matter of degree
# normal ----- meltdown
# python is on the normal side

# EXCEPTIONS AND CONTROL FLOW
# for use on repl using exceptions import
# from exceptional import convert
# since working on idea workspace that isn't needed
# just paste the function into here, also I couldn't get it to work


def convert(s):
    """convert to integer"""
    x = int(s)
    return x


print(convert("33"))
# if trying to convert an object of non type int
# exception raised, trace call sent
# since no handler was present it was caught by repl and stack trace was displayed
'print(convert("test"))'  # ValueError
"""
ValueError: invalid literal for int() with base 10: 'test'
----------  ----------------------------------------------
Value error was type of exception object, the what
is the payload retrieved by repl, the why (though can't go into depth and solve the problem)
"""
# the error crosses many levels of call stack
"""
1 - the call for the int() constructor, stating the error and why
2 - the covert() function stating what has been said by the int(), passing it off to next level
3 - the repl witch takes the information and formulates raised exception, raised exception experienced by program
"""

# HANDLING EXCEPTIONS
# update to convert function
# now handles the exception of ValueError
# uses try-except construct
# format:
"""
try:
    block of code that could contain an exception
except Error:
    block of code (ran if error is raised)
"""
# EX:


def convert(s):
    """convert to integer"""
    try:
        x = int(s)
        print("conversion succeeded x =", x)
    except ValueError:
        print("conversion failed")
        x = -1
    return x


# testing the exception handler
# EX:
print(convert("45"))
print(convert("test"))
# print after the integer conversion was not output
# this is because an exception was thrown and went to handler before getting to next part in block
# in the convert handler, if fed another type like list another type of error is thrown, TypeError
'print(convert([5, 8, 2]))'  # TypeError
# each try block can have multiple except blocks to lead to different blocks for different errors
"""
try:
    block of code that could contain an exception
except Error:
    block of code (ran if error is raised)
except AnotherError:
    block of code (ran if error a different error is raised that isn't excepted by other blocks)
except ...
...
"""


def convert(s):
    """convert to integer"""
    try:
        x = int(s)
        print("conversion succeeded x =", x)
    except ValueError:
        print("conversion failed")
        x = -1
    except TypeError:
        print("conversion failed")
        x = -2
    return x


# EX:
# same line that raised error
# though now has a TypeError exception handler
print(convert([5, 8, 2]))
# to help avoid code duplication, set the variable reference to default prior
# then set it to another value if no error is raised, else wise when error is thrown it will still be default
# also, if any number of exception blocks have the same blocks of code, those blocks can be combine to one
# the handler will accept a tuple of exception types
# the errors will lead to the same block
# syntax:
"""
except (OneError, TwoError, ...):  # tuple of exception types
    block of code (runs for all errors in handler statement)
"""


def convert(s):
    """convert to integer"""
    x = -1
    try:
        x = int(s)
        print("conversion succeeded x =", x)
    except (ValueError, TypeError):
        print("conversion failed")
    return x


# EX:
print(convert("111"))
print(convert("test"))
print(convert(["4", "6"]))

# PROGRAMMER ERRORS
# flow signals aren't necessary to handling, just helpful
"""
def convert(s):
    '''convert to integer'''
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError):  # must be indentation after except block, IndentationError raised
    return x  # must be indentation after except block, IndentationError raised
"""
# but when an except block is empty another type of error is thrown, programmer errors
# programmer errors are types of errors that aren't handled
# others like IndentationError, SyntaxError, and NameError are a few
# these should be corrected during development rather than handled at runtime
# EX:
# to prevent this IndentationError a keyword "pass" should be put in the empty block
# pass is nothing, allows blocks to be permissibly empty - meaning the program just passes right through it


def convert(s):
    """convert to integer"""
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError):
        pass
    return x


print(convert("333"))
print(convert("test"))
print(convert(["4", "6"]))
# EX:
# though in this case, to simply further the except could return the int() or -1 using multiple return statements
# the default statement isn't really needed because all the program did was return either the int() if converted
# and -1 if not
# this is then coupled with the flow signals not present anymore


def convert(s):
    """convert to integer"""
    try:
        return int(s)
    except (ValueError, TypeError):
        return -1


print(convert("444"))
print(convert("test"))
print(convert(["4", "6"]))
# to then get more details on the error raised the as keyword can be used to set a variable of error information
#  pass the exception object as a string, str(e)
# to then output this information use the "sys" module
# then using the sys module, can then get the standard error "sys.stderr" and set to keyword file, file=sys.stderr
# all exception objects can be passed as a string to show what kind of error it is, the why
# sys.stderr has to do with where python's exception are written to
# it is useful to print the error to stream
# (i think it is like files that have everything going on in the program)
# (so it would have what error happen)
# (so it is passed to file keyword because it is a file containing the exception)
import sys


def convert(s):
    """convert to integer"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("conversion error: {}".format(str(e), file=sys.stderr))
        return -1


print(convert("fail"))

# IMPRUDENT ERROR CODES
# exceptions can not be ignored
# the function is unpythonic, overall bad
# the int() conversion is hidden in the function that returns -1 as an exception
# this will lead to the log failure and lead to raising of another exception
# EX:
# implement a new function that outputs the convert functions return to a log
# using the math module, log function
from math import log


def string_logs(s):
    v = convert(s)
    return log(v)


# output responses
# normal response
print(string_logs(81))
# exception raised response
'print(string_logs("test"))'  # ValueError: math domain error
# better to forget about error codes and go back to raising exception from convert

# RE-RAISING EXCEPTIONS
# instead of returning a possible issued return, the error currently being handled can be re-raised
# so if it throws an exception of ValueError in the handling exception block, it can then be raised again to the block
# this can be done with the "raise" keyword


def convert(s):
    """convert to integer"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("conversion error: {}".format(str(e), file=sys.stderr))
        raise


# the error message is still raised causing issues
# but the ValueError exception handler raised again
# the conversion error message is printed after the issue error message
# so it outputs raised exception and the why
'print(string_logs("test-t"))'

# EXCEPTIONS AS API
# exceptions are important to api of function
# callers need to know what exceptions to expect, and when
# so that exception handlers are in place
# EX:
# using a square root function
# a home grown square root function that demonstrates importance of exception handlers
# and operator tests if both conditions are true
# the or operator tests if at least one is true


def sqrt(x):
    """
    Compute square roots using the method of Heron Alexandria.

    Args:
        x: The number for which the square root is computed.
    Returns:
        The square root of x.
    """
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    print(sqrt(9))
    print(sqrt(2))
    # when adding new line testing -1, meet with an error
    # occurs on this from a division by zero during the second iteration of the loop
    # from guess being set to 0 from (-1 + 1) / 2 -> 0 / 2 -> 0 = guess
    'print(sqrt(-1))'  # ZeroDivisionError exception


if __name__ == '__main__':
    'main()'


def main():
    # to help limit the issue, can add a handler in the main() function
    # it will handle the ZeroDivisionError
    # the program will handle the error and then continue normally through the function
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ZeroDivisionError:
        print("Cannot compute square root of a negative number.")
    print("Continuing normally now.")


if __name__ == '__main__':
    main()


# this function can then be modified further
# it is better to include all calls of the sqrt() function to be enclosed in the try block
# but once except block is called, everything everything after the statement that raised the exception is never executed


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never printed.")
    except ZeroDivisionError:
        print("Cannot compute square root of a negative number.")
    print("Continuing normally now.")

# use exceptions that user will anticipate
# standard exceptions are often the best choice, this means use exceptions that are common, ValueError, TypeError
# python provides many standard execution types
# if a parameter is supplied illegal value, it is custom to raise ValueError
# this can be done by using the "raise" keyword to raise a ValueError with the ValueError() constructor
# this makes two ways to approach the ZeroDivisionError:
# first being to raise the ValueError() in the except ZeroDivisionError block in the sqrt() function
# this new function will raise a ValueError


def sqrt(x):
    """
    Compute square roots using the method of Heron Alexandria.

    Args:
        x: The number for which the square root is computed.
    Returns:
        The square root of x.
    """
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x / guess) / 2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess


# this function would be wasteful though
# the better method to handling this would
# it would be better to test if number is negative and then raise a ValueError and state why
# the ValueError constructor accepts an error message as a parameter
# this is also included in the docstring as Raises of the function
# in doing this the function will now raise a ValueError() and can be handled by an outside handler


def sqrt(x):
    """
    Compute square roots using the method of Heron Alexandria.

    Args:
        x: The number for which the square root is computed.
    Returns:
        The square root of x.
    Raises:
        ValueError: If x is negative.
    """
    # added this to handle all typeError exceptions
    # if the type is neither int or float it will raise a ValueError
    # now learning that this is not ideal - do not guard against type errors
    # still going to keep it but bad programming practice, cant use complex, fractional, etc...
    if type(x) != int and type(x) != float:
        raise ValueError(f"Cannot compute this type {type(x)}.")
    elif x < 0:
        raise ValueError(f"Cannot compute square root of negative number {x}.")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


# the outside handler must now be modified, main()
# now that is has a common ValueError(), the function can now use one handler for dividing by zeros and value difference
# we can then use the error message sent by sqrt to alter the message output to state whether it is dividing by zero
# or a regular ValueError
# we now use the as operand to set the ValueError error message to a variable and use sys.stderr
# to get the file of errors happening in the program and output the error
# this message could either be from a value which would be caught in main
# or from dividing by zero which would be raised as a valueError in sqrt but constructed with a different error and
# then handled by the ValueError handler but with the variable e now referencing the error message constructed in sqrt
import sys


def main():
    try:
        print("start")
        print(sqrt(9))
        print(sqrt(2))
        # both raise valueErrors
        'print(sqrt(-1))'  # valueError raised because of zero division
        's = int("k")'  # valueError raised because of valueError
        'print(sqrt("s"))'  # valueError raised because of TypeError
    except ValueError as e:
        print("{}".format(e, file=sys.stderr))
    print("Continuing normally now.")


if __name__ == '__main__':
    main()


# EXCEPTIONS, APIS, AND PROTOCOLS
# exceptions are part of families of related functions referred to as "protocols"
# this means objects in certain protocols discussed at the end of last module should raise certain exceptions
# certain protocols go with certain exceptions
# -like anything a part of sequence protocol should raise an IndexError to handle indexes out of range
# the exceptions of a function are as important as the arguments and function of the function
# this means it should be implemented and documented correctly
# use the common or existing exception types when possible
# it is possible to create own exception types but it will be in a more advanced course
# to find which exceptions you code should raise, look for similar cases in existing code
# the more the code follows standards, the easier it will be to implement and understand
# this means use standards everyone else follows making it easy for others to view and understand the code
# EX:
# use keyError when using a key value database to display if someone has requested an unknown key, like a dictionary
# mapping in python follows certain patterns and exceptions are apart of that pattern
# common errors:
"""
IndexError: when integer index is out of range
ValueError: object is of right type but contains inappropriate value
KeyError: look-up in a mapping fails
etc...
"""

# DO NOT GUARD AGAINST TYPE ERRORS
# avoid protecting against TypeErrors
# this is because it limits the use of re-using code
# EX:
# can test is argument is a string with isinstance(s, type), takes 2 arguments the first being the variable and
# second being the type testing for
# it returns true if the variable is the type
# then raise a TypeError if it is not
# this then raises issues for program when wanting to allow instances of float as well, and then others like
# fraction, complex, etc...
# it is typical to allow function to work with particular type
# then to just allow it to fail with other types, even so it would still probably result in a TypeError
# not worth checking types
# this can limit function unnecessarily


def convert(s):
    """Convert to integer."""
    if not isinstance(s, str):
        raise TypeError("Argument must be a string")
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("".format(e, file=sys.stderr))
        raise


# this avoidance stems from not knowing what types should or will work with program so it would be best to
# removing testing the type and trying to Raise a type error and letting it fail and catch if it doesn't work


def convert(s):
    """Convert to integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("".format(e, file=sys.stderr))
        raise


""

# EAFP VS. LBYL
# python culture, easier to ask for forgiveness than permission
# two approaches tot dealing with program that might failure:
"""
'L'ook 'B'efore 'Y'ou 'L'eap or LBYL
first - check that all preconditions for a failure prone operation are met,
this means just make sure everything is ready for operation and information is perfectly correct
that it will work fine
It's 'E'asier to 'A'sk 'F'orgiveness than 'P'ermission or EAFP
second - hope for best and prepare for consequences if it doesn't work out,
this means don't check for much but be ready for any exceptions thrown
"""
# python favors the philosophy of EAFP because the happy path in its most readable form with deviations from the normal
# flow handled separately rather than interspersed with main flow
# python is more EAFP based because it throws exceptions that can then be handled non-locally (outside the main flow)
# and are not easily ignored, allows main flow to run fine but can be handled at anytime from outside logic
# EX:
# processing a file just
# os module import is used to work with files
# the process_file(file) function opens a file and reads it
# the LBYL version
# the program checks if file exists and if it doesn't it states a message
import os

p = '/path/to/datafile.dat'

if os.path.exists(p):
    'process_file(p)'  # process_file won't work
else:
    print('No such file as {}'.format(p))


# some issues arise though
# this is just an existence check
# this is just one issue that would have to be checked for, we would also have to check if its a directory, or garbage
# using this mindset, preemptive test should be added to test for these as well
# another subtle issue is that the file could be altered or deleted between checking for existence and processing
# atomicity issue in the open block of code
# now using EAFP approach:
# this approach doesnt test for anything but catches the error if anything goes wrong, file doesnt exist, directory, etc
p = '/path/to/datafile.dat'

try:
    'process_file(p)'  # process_file won't work
except OSError as e:
    print("Could not process file because {}". format(str(e)))


# OSError catches everything that has to do with working with a file
# since exceptions interrupt the flow of program, it allows you to handle them non-locally and continue with main flow
# using error codes, or checking preconditions, interrupts main flow of program
# error codes require interspersed, local handling
# exceptions allow centralized non-local handling
# this therefore makes python eafp with exceptions allowing you to interrupt the program when one is raised
# and to then handle it non-locally away from main flow of program
# exceptions require explicit handling, meaning they cannot be easily ignored
# error codes through are silent and can be ignored without ever noticing
# error passing silently means the error is not raised and handled by caller, meaning exception block handles it
# this means leaving it up to exceptions and eafp, the errors and issues cannot be easily ignored

# CLEAN-UP ACTIONS
# resource cleanup with finally
# try...finally lets you clean up whether an exception occurs of not
# useful with context managers
# EX:
# a program that changes to a directory creates a new directory and then returns to original directory
import os


def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    os.mkdir(dir_name)  # if this fails
    os.chdir(original_path)  # this won't happen


# an issue with this program could be that should mkdir fail at any point, the program will fail to
# return to original directory
# to fix this we would like to set the current directory to the original directory and try to change and make
# and even if either fail or succeed, the finally block will execute bringing us back to original directory
# code in finally block is reached by either flow at end of try block or exceptionally by the raise of an exception


def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    finally:
        os.chdir(original_path)


# the try...finally construct can be combined with except blocks
# it will work the same as at end of try it will go to finally, but if exception is raised, it will be handled
# then re-raised and then control will be given to finally block, try...except...finally
# should always re-raise after handling exceptions to show other uses of function that error has been raised and output
# error message
# even though full exception was raised, the finally block still executed
import os
import sys


def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        print("tst")
        os.chdir(original_path)


'print(make_at("", ""))'  # even though error is raised and throws code off, "tst is still output"
""

# PLATFORM-SPECIFIC CODE
# an example of a platform specific code is the press any key to continue at console
# EX:
# to do this on windows msvcrt is required
# while on linux and osx, sys, tty, and termios can be used
# the program tries to to use a import module for keypress in windows
# the program then uses an importError to check if system is windows and if error is raised from importing msvcrt
# to then start the exception block use other method of importing other platform-specific modules for unix based systems
# the importError for one module specific triggers the exception block with import code for other platform


"""keypress - A module for detecting a single keypress."""

try:
    import msvcrt

    def getkey():
        """Wait for a keypress and a return a single character string"""
        return msvcrt.getch()

except ImportError:

    import sys
    import tty
    import termios

    def getkey():
        """Wait for a keypress and a return a single character string"""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcgetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch

    # if either of the Unx-specific tty or termios are not found,
    # we all the ImportError to propagate from here
''

# all top level module code is executed on first import
# all top level code is code not executed first on run, functions classes
# within the first try: block the microsoft visual c runtime or msvcrt
# if this succeeds it will then create a function getkey() which wil get keypress
# even though it is declared in try, try is the scope of the outer container being the module scope
# this means the function is declared throughout the module
# if however the import fails, because not running on windows the ImportError will be raised
# execution will then be transferred to except ImportError block
# -though this is a case of an error being silenced because it is alternatively attempt a course of action for getkey()
# import three modules needed for getkey implementation on unix systems
# then proceed to alternative def of getkey
# this getkey fucntion is created in the except block but is within the module scope so is declared through the module
# this unix implementation of getkey uses a try...finally to go into raw mode and get input from terminal from single ch
# if neither running on windows or unix, the import tty will raise as second error, though this will not be silencd
# it will then be up to the caller, which is whatever imported this module, if caller can take action it can with error
# the module signals this this error but up to caller on what to do with it,
# therefore the error will not pass silently

# TESTING
# try convert functions
# try exercise file in pythonReLearn
# use things like raising to common exceptions, sending raise to caller function for output, eafp
# exercise.py


def convert_f(num):
    try:
        return int(num)
    except (ValueError, TypeError) as err:
        raise ValueError(err)


x = input("---- ")

print(convert_f(x))



