#!C:\Python_Work\Learning\Python_Fundamentals
"""
A program that determines seating on a bus by setting up buses' rows and seats in each and then
assigning names to each seat. Can also remove names from a search through the whole bus of a name.
"""

bus = []


def setting_up_bus():
    """
    Used to set up seating rows and seating on bus.
    Can set up bus with the same and different amounts of seats in each row.
    """
    bus_row = data_valid("How many rows are on the bus? ") - 1
    while True:
        same_rows = get_string("Does each row have the same number of seats: YES or NO ")
        if same_rows.upper() == "YES":
            calc_seating(bus_row, "YES")
            break
        elif same_rows.upper() == "NO":
            calc_seating(bus_row, "NO")
            break


def calc_seating(row_number, input_row):
    """
    Calculates the seats in each row, either all being the same or differing.

    Args:
        row_number: Amount of rows in bus.
        input_row: Determines if rows have same number of seats.
    """
    i = 1
    if input_row == "YES":
        bus_seats = data_valid("How many seats per row? ") - 1
        while row_number >= 0:
            bus.append({"row": i, "seat": gen_list(bus_seats)})
            i += 1
            row_number -= 1
    while row_number >= 0 and input_row == "NO":
        row_seats = data_valid(f"Enter amount of seats for row number {i}: ") - 1
        bus.append({"row": i, "seat": gen_list(row_seats)})
        i += 1
        row_number -= 1


def gen_list(seats):
    """
    Used to generate a list to be copied back into calc_seating for number of seats.

    Args:
        seats: The amount of seats that will be added to list.
    """
    seat_list = []
    k = 1
    while seats >= 0:
        seat_list.append(k)
        k += 1
        seats -= 1
    return seat_list


def seating():
    """
    Find an open seat.
    Remove a seat by input of name.
    Exit command for seating procedure.
    Checks if bus is full.
    """
    while True:
        flag = full_check()
        while flag:
            while True:
                bus_options = get_string("Would you like to remove seats: "
                                         "REMOVE or EXIT ")
                if bus_options.upper() == "REMOVE":
                    seat_remover()
                    flag = False
                    break
                elif bus_options.upper() == "EXIT":
                    return
        bus_options = get_string("Would you like to find or remove seats: "
                                 "FIND, REMOVE, or EXIT ")
        if bus_options.upper() == "FIND":
            find_seat()
        elif bus_options.upper() == "REMOVE":
            seat_remover()
        elif bus_options.upper() == "EXIT":
            return


def find_seat():
    """
    Do data validation and find an open seat.
    Assign name to the seat.
    Exit statement.
    """
    while True:
        print("*enter a 0 to exit the selection process*")
        select_exit = False
        while True:
            row_in = data_valid("What row do you want: ") - 1
            if step_through_index_count(row_in, bus):
                break
            elif row_in == -1:
                select_exit = True
                break
        if select_exit:
            break
        row = bus[row_in]["seat"]
        open_seats = 0
        print(f"Now accessing row {bus[row_in]['row']}.")
        for seat in row:
            if step_through_whole_count(seat, row):
                print(f"Seat number {seat} is open.")
                open_seats += 1
            else:
                print(f"This seat is taken by {seat}.")
        if open_seats > 0:
            seat_validation(row)
            break
        else:
            print("The row is full. Sorry pick another one.")


def full_check():
    """
    Checks if all the seats on bus are taken up.

    Returns:
        Returns True if bus is full and False if not full.
    """
    open_seats = 0
    for i in bus:
        for seat in i["seat"]:
            if step_through_whole_count(seat, i["seat"]):
                open_seats += 1
    if open_seats == 0:
        print("The bus is full.")
        return True
    return False


def seat_remover():
    """
    Finds seat by name to remove.
    """
    name = get_string("What is the name in your seat: ")
    found = False
    for i in bus:
        k = 0
        for seat in i["seat"]:
            k += 1
            if seat == name.capitalize():
                print(f"The seat with name {seat} in row {i['row']}, "
                      f"seat {k}, will now be removed.")
                i["seat"][k - 1] = k
                found = True
                break
        if found:
            break
    if not found:
        print(f"The seat with name {name.capitalize()} could not be found.")


def seat_validation(row):
    """
    Finds open seats in row to take and add user name to.

    Args:
        row: The row currently being looking into.
    """
    while True:
        while True:
            sitting = data_valid("What of the open seats do you want: ") - 1
            if step_through_index_count(sitting, row):
                break
        if step_through_whole_count(row[sitting], row):
            row[sitting] = get_string("What is your name: ").capitalize()
            break


def data_valid(text):
    """
    Validates numerical whole number data.

    Args:
        text: Text to show user.
    Returns:
        Returns the valid number.
    """
    while True:
        x = input(text)
        if x.isdigit():
            return int(x)


def get_string(text):
    """
    Validates a string.

    Args:
         text: Text to show user.
    Returns:
        Return the valid string.
    """
    while True:
        y = input(text)
        if y.isalpha():
            return y


def step_through_index_count(element_in, elements_list):
    """
    Validates openness in the row by comparing chosen input to list of open inputs.
    Steps through starting with 0 for index number check.

    Args:
        element_in: The element input.
        elements_list: The list of elements to compare to.
    Returns:
        Return True if the input was open and False if it not available.
    """
    y = 0
    while y < len(elements_list):
        if element_in == y:
            return True
        y += 1
    return False


def step_through_whole_count(element_in, elements_list):
    """
    Validates openness in the row by comparing chosen input to list of open inputs.
    Steps through starting with 1 for whole number check.

    Args:
        element_in: The element input.
        elements_list: The list of elements to compare to.
    Returns:
        Return True if the input was open and False if it not available.
    """
    y = 1
    while y <= len(elements_list):
        if element_in == y:
            return True
        y += 1
    return False


if __name__ == "__main__":
    """
    Source flow for the program.
    """
    setting_up_bus()
    seating()
    print(bus)
