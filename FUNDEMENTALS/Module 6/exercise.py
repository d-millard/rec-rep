import os
import sys
# import fileinput
# was going to use these things for like fileinput and the sys.stderr
"""
made everything work only in the C:\\Test\\ directory for ease of use
"""


def get_file(text):
    """
    Validates if the file is in the directory, if not fives option to create.
    # not sure but think using with in this context helps clean up the resource

    Args:
        text: the text to be used in the ask input
    Returns:
        The open file object.
    Raises:
        ValueError: raises ValueError for commonality but displays altered File not found message
    """
    path = input(text)
    try:
        with open(f"C:\\Test\\{path}.txt") as f:
            return f
    except (FileNotFoundError, PermissionError) as e:
        print("This File has not been found, would you like to create it?")
        while True:
            choice = input("(YES or NO): ")
            if choice.lower() == "yes":
                return open(f"C:\\Test\\{path}.txt", "w")
            elif choice.lower() == "no":
                raise ValueError(f"File not found: {e}")


def convert_int(text):
    """
    Converts whatever input from user into integer.

    Args:
        text: the text to be used in the ask input
    Returns:
        the valid int number
    Raises:
        ValueError: (zero) if the number is below 0, can't have less than 1 file
        ValueError: (Conversion) if the input from user cannot be converted into an int
    """
    num = input(text)
    try:
        if int(num) <= 0:
            raise ValueError("Number must be a whole number above zero.")
        return int(num)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Conversion error: {e}")


def file_check(final_files_list, file):
    """
    Checks if file just input is the same as another file input already.

    Args:
        final_files_list: list of current valid files input, not one being added currently.
        file: the file input.
    Raises:
        ValueError: raises this error for commonality but states files
                    can not be the same, exception stops file append.
    """
    for check in final_files_list:
        if check.name == file.name:
            raise ValueError("Files cannot be the same.")


def main():
    """
    Controls all the programs input flow.
    Handles the commonality raises of ValueError.
    Gets the number of files and each valid file and sends information to be processed
    in process_file() function.
    """
    while True:
        try:
            num_of_files = convert_int("How many files do you want to input: ")
            break
        except ValueError as e:
            print(e)
    files_list = [None] * num_of_files
    final_files_list = []
    for index in enumerate(files_list, 1):
        while True:
            try:
                file = get_file(f"Please input the name of file #{index[0]} : ")
                file_check(final_files_list, file)
                final_files_list.append(file)
                break
            except ValueError as e:
                print(e)
    process_file(final_files_list)


def process_file(final_files_list):
    """
    Processes the file getting whether it will be read, written, closed, or removed.
    Loops until file is closed or removed.

    Args:
        final_files_list: list of all valid files
    """
    for index, file in enumerate(final_files_list):
        file_name = file.name.split("\\")[-1]
        file_path = '\\'.join(file.name.split("\\")[:-1])
        print(f"Now accessing File: {file_name} on Path: {file_path}")
        print("What operations would you like to carry out on file?")
        while True:
            choice = input("READ, WRITE(override), APPEND(add to), REMOVE, or CLOSE: ")
            if choice.lower() == "read":
                read(file)
            elif choice.lower() == "write":
                write(file)
            elif choice.lower() == "append":
                append(file)
            elif choice.lower() == "close":
                final_files_list[index] = file.close()
                print("File closed.")
                break
            elif choice.lower() == "remove":
                """
                getting a lot of issues with os.remove() os the PermissionError will handle the weird stuff
                don't really understand but the print()s help a lot on close an remove for some reason
                os.remove() wouldn't even work on my system without the print("File removed.")
                --further testing and knowledge is needed--
                issues with created files in the program, can't delete them at all
                """
                try:
                    os.remove(file.name)
                    print("File removed.")
                    break
                except PermissionError as e:
                    print(e, sys.stderr)


def append(file):
    """
        Appends to current file being worked on.
        Uses a temp reference file so actual reference doesn't run into issues about being closed.

        Args:
            file: the file to be written to
        """
    input_list = file_input("What would you like to append to the text file: ")
    temp = open(file.name, "a")
    temp.write("\n")
    for i in input_list:
        temp.write(f"{' '.join(i)}\n")
    temp.close()


def read(file):
    """
    Reads the text off the file.
    Uses a temp reference file so actual reference doesn't run into issues about being closed.

    Args:
        file: the file to be read
    """
    temp = open(file.name)
    print(f"\n{temp.read()}")
    temp.close()


def write(file):
    """
    Writes to current file being worked on.
    Uses a temp reference file so actual reference doesn't run into issues about being closed.

    Args:
        file: the file to be written to
    """
    input_list = file_input("What would you like to write to the text file: ")
    temp = open(file.name, "w")
    for i in input_list:
        temp.write(f"{' '.join(i)}\n")
    temp.close()


def file_input(text):
    """
    Cuts each line off after 50 character, doesn't cut words - goes up.

    Args:
        text: text to be used when asking user to input
    Returns:
        final_list: the list of all lines going to be written or appended
    """
    text_input = input(text)
    text_list = text_input.split()
    final_list = []
    total, count, iterations = 0, 0, 0
    for ind, i in enumerate(text_list):
        for _ in i:
            total += 1
        if total >= 50 and final_list == []:
            final_list.append(text_list[:ind])
            count += len(final_list[iterations])
            iterations += 1
            total = 0
        elif total >= 50:
            final_list.append(text_list[count:ind])
            count += len(final_list[iterations])
            iterations += 1
            total = 0
        elif ind == (len(text_list) - 1) and final_list == []:
            final_list.append(text_list)
        elif ind == (len(text_list) - 1) and total > 0:
            final_list.append(text_list[count:])
    return final_list


if __name__ == '__main__':
    """ Work flow of the program if run as the main, not imported. """
    main()
                   
