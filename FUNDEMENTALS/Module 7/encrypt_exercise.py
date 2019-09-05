from random import random as ran
import os


def run():
    """
    Main function for program.
    Brings together files, all symbols, the unicode hexadecimal, and the key.
    """
    while True:
        try:
            user_data = user_file("Please enter a valid file name you would like to encrypt: ")
            f_temp = open("C:\\Test\\f_temp.txt", "w")
            break
        except ValueError as e:
            print(e)
    symbols = read_lines(user_data.name)
    ref = dict()
    for key in symbols:
        for value in (k for k in (item for item in uni_gen()) if str(chr(int(k, 16))) == key):
            while True:
                random = random_code()
                if code_check(ref, random):
                    print(f"Now encrypting {value}.")
                    ref[str(chr(int(value, 16)))] = random
                    break
    write_copy(user_data.name, f_temp.name, ref)
    write_source(user_data.name, f_temp.name)
    f_temp.close()
    os.remove(f_temp.name)
    print("         key")
    for key, value in ref.items():
        print(f"        {key} = {str(chr(int(value, 16)))}")


def uni_gen(end=81):
    """
    A generator to generate the unicode hexadecimal numbers.

    Args:
        end: optional. default english lexicon. can add more or littler characters
    Yields:
        the hexadecimal number
    """
    yield r"0x0020"
    for i in range(21, end):
        if i % 10 != 0:
            yield r"0x00{}".format(str(i))
        else:
            for a in ("A", "B", "C", "D", "E", "F"):
                yield r"0x00{}{}".format(str(i - 1)[0], a)
            yield r"0x00{}".format(str(i))


def code_check(ref, random):
    """
    Checks if the random hexadecimal number is already in the ref dictionary as a random code.

    Args:
        ref: a reference dictionary of all characters and random hexadecimal codes
        random: the random hexadecimal code generated
    Returns:
        bool of whether or not it is already a code
    """
    for _, v in ref.items():
        if v == random:
            return False
    return True


def random_code(string=None):
    """
    Generates a random code.

    Args:
        string: initializes the string argument
    Returns:
        the string argument of the random hexadecimal
    """
    ran_gen = uni_gen()
    for i in range(int(1 + ran() * 97)):
        string = next(ran_gen)
    return string


def read_lines(name):
    """
    Reads all characters in document and adds to set.
    Set filters to be all unique characters in file.

    Args:
        name: name of file to open for reading
    Returns:
        the set of all unique characters
    """
    temp = open(name, "r")
    symbols = set()
    try:
        while True:
            string = next(temp).replace("\n", "")
            for characters in string:
                symbols.add(characters)
    except StopIteration:
        temp.close()
        return symbols


def write_copy(name, copy, ref):
    """
    Writes encryption to a temporary file to be copied to source.

    Args:
        name: name of file to open for reading
        copy: name of file to write to temporarily
        ref: a reference dictionary of all characters and random hexadecimal codes
    """
    temp = open(name, "r")
    f_temp = open(copy, "w")
    try:
        while True:
            string = next(temp).replace("\n", "")
            for characters in string:
                f_temp.write(ref[characters])
    except StopIteration:
        temp.close()
        f_temp.close()


def write_source(name, copy):
    """
    Writes encryption from temporary file to source file.

    Args:
        name: name of file to open for writing
        copy: name of file to read from temporarily
    """
    f_temp = open(copy, "r")
    temp = open(name, "w")
    try:
        while True:
            string = next(f_temp)
            temp.write(string)
    except StopIteration:
        f_temp.close()
        temp.close()


def user_file(text):
    """
    Validates user input file.

    Args:
        text: text to prompt user
    Returns:
        the valid file
    """
    try:
        with open(input(text)) as f:
            return f
    except (PermissionError, FileNotFoundError) as e:
        raise ValueError(e)


if __name__ == '__main__':
    """source flow for program"""
    run()
