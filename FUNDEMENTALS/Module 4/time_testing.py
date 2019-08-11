#!C:\Python_Work\Learning\Python_Fundamentals
"""
A program that calculates the time and date in a well formatted format for anything year, month, 24 hour time.
It also uses an algorithm to find the weekday for any day with no use of database.
"""
# time import that is used to output a current time tuple to be formatted
import time


def time_input():
    """
    The work flow for the time program.
    Get whether use wants to use the calculator, if current or custom time, and if they wan't to re-run.
    """
    exit_time = False
    while not exit_time:
        input_choice = text_valid("Would you like to access the time/date calculator? YES or NO ")
        if input_choice.upper() == "YES":
            while True:
                custom_val = text_valid("Would you like to input a custom time/date "
                                        "or use the current one? CURRENT or CUSTOM ")
                if custom_val.upper() == "CUSTOM":
                    custom_choice()
                    re_run_choice = text_valid("Would you like to calculate another? YES or NO ")
                    if re_run_choice.upper() == "YES":
                        ""
                    else:
                        exit_time = True
                        break
                elif custom_val.upper() == "CURRENT":
                    time_format()
                    re_run_choice = text_valid("Would you like to calculate another? YES or NO ")
                    if re_run_choice.upper() == "YES":
                        ""
                    else:
                        exit_time = True
                        break
        elif input_choice.upper() == "NO":
            break


def custom_choice():
    """
    Central flow for all of custom inputs.
    Uses list of dictionaries for references to then apply logic, all logic and algorithms use these as reference.
    Gets the year, month, time (hour and min) by user input.
    Gets the weekday from calculations on reference data of the year 2000 the leap/regular years.
    Gets the total though background calculations.
    Gets the daylight savings signal through background calculations.
    """
    # monday - sunday, year 2000 ref
    ref_year_twok = [
        {'start_days': False, 'position': 0},
        {'start_days': False, 'position': 1},
        {'start_days': False, 'position': 2},
        {'start_days': False, 'position': 3},
        {'start_days': False, 'position': 4},
        {'start_days': True, 'position': 5},
        {'start_days': True, 'position': 6}
    ]
    # get the year, leap years, and regular years
    get_year = number_valid("Please enter the year: ")
    year_change = None
    leap_year = 0
    reg_year = 0
    if get_year < 2000:
        year_change = False
        get_year_dif = 2000 - get_year
        while get_year_dif > 0:
            if get_year_dif % 4 == 0:
                leap_year += 1
            else:
                reg_year += 1
            if get_year_dif % 400 != 0 and get_year_dif % 100 == 0:
                leap_year -= 1
                reg_year += 1
            get_year_dif -= 1
    elif get_year > 2000:
        year_change = True
        get_year_dif = get_year - 2000
        # use index of 0 for first year after leap to have extra 2 days, if 1 is used the year itself will have 2 days
        # 0 % 4 == 0 is True
        # this makes each run with an index of year before, then add that years index after - EX: 2004 will run with 3
        index = 0
        while get_year_dif > 0:
            if index % 4 == 0:
                leap_year += 1
            else:
                reg_year += 1
            if index % 400 != 0 and index % 100 == 0:
                leap_year -= 1
                reg_year += 1
            get_year_dif -= 1
            index += 1
    months = [
        {'Month': "January", 'Days': 31},
        {'Month': "February", 'Days': 29 if leap_year_determination(get_year) else 28},
        {'Month': "March", 'Days': 31},
        {'Month': "April", 'Days': 30},
        {'Month': "May", 'Days': 31},
        {'Month': "June", 'Days': 30},
        {'Month': "July", 'Days': 31},
        {'Month': "August", 'Days': 31},
        {'Month': "September", 'Days': 30},
        {'Month': "October", 'Days': 31},
        {'Month': "November", 'Days': 30},
        {'Month': "December", 'Days': 31}
    ]
    # get the month number and name
    while True:
        while True:
            get_month = input("Please enter the month (numbered or named): ")
            if get_month.isdigit() or get_month.isalpha():
                break
        try:
            if 0 < int(get_month) <= 12:
                get_month_name = months[int(get_month) - 1]["Month"]
                get_month = int(get_month)
                break
        except ValueError:
            ""
        try:
            if month_check(months, get_month):
                get_month_name = get_month
                get_month_name = get_month_name.capitalize()
                i = 0
                for month in months:
                    if get_month_name.capitalize() == month["Month"]:
                        get_month = i + 1
                        break
                    i += 1
                break
        except ValueError:
            ""
    get_day = get_day_func(get_month_name, months, get_month)
    # get the time (hour and min)
    while True:
        u_time = input("Please enter the 0 - 23 hour time (use [hh:mm] format): ")
        get_hour = u_time[0:2]
        get_min = u_time[3:5]
        if len(u_time) == 5 and (u_time.find(":") != -1) and get_hour.isdigit() and get_min.isdigit():
            if 0 <= int(get_hour) < 24 and int(get_min) <= 59:
                break
    # monday - sunday weekdays (monday being the first [1], sunday being last [0] because modulus by 7)
    weekdays = [0, 1, 2, 3, 4, 5, 6]
    calc_first_week(year_change, reg_year, leap_year, ref_year_twok)
    get_total = get_total_func(get_day, months, get_month_name)
    get_wday = weekdays[set_first_week(ref_year_twok, get_total)]
    get_daylight_time = int(get_hour + get_min)
    start_total = months[0]["Days"] + months[1]["Days"]
    start_daylight = get_daylight_savings(ref_year_twok, weekdays, start_total, 1)
    end_total = ((366 if leap_year_determination(get_year) else 365)
                 - (months[10]["Days"] + months[11]["Days"]))
    end_daylight = get_daylight_savings(ref_year_twok, weekdays, end_total, 0)
    get_daylight = daylight_savings_calc(start_daylight, end_daylight, get_total, get_daylight_time)
    custom_time = (get_year, get_month, get_day, int(get_hour), get_min, get_wday, get_total, get_daylight)
    time_format(custom_time)


def get_daylight_savings(ref_year_twok, weekdays, total, stop):
    """
    Gets reference days for daylight savings, (start and end).
    March will always be second sunday while Novembers will be the first sunday.

    Args:
        ref_year_twok: the altered 2000 reference year
        weekdays: the numerical values for the weekday
        total: the total days before the month of the month of daylight saving
        stop: when to stop, either first or second time seen
    Returns:
        i + total: the final referenced day
    """
    x = 0
    i = 0
    while i < 32:
        for weekday in ref_year_twok:
            if (total + i) % 7 == weekday['start_days']:
                wday_pos = weekday['position']
                if weekdays[wday_pos] == 6:
                    if x == stop:
                        return i + total
                    x += 1
                    break
        i += 1


def get_day_func(get_month_name, months, get_month):
    """
    A function to get the day from the user and validate it.

    Args:
        get_month_name: the name of the month input from user
        months: a reference of all months with references of their days for reference
        get_month: the numerical value of the month
    Returns:
        get_day: the valid day from the user
    """
    while True:
        get_day = number_valid(f"Please enter the day for {get_month_name}: ")
        if 0 < get_day <= months[get_month - 1]["Days"]:
            return get_day


def get_total_func(day, months, get_month_name):
    """
    A function that gets the total days in the year from the day the user input.

    Args:
        day: the valid day input by the user
        months: a data set of the months' titles and respective days
        get_month_name: the name of the month input by user
    Returns:
        get_total: the total amount of days in the year of users input data
    """
    get_total = day
    for month in months:
        if month['Month'] == get_month_name:
            return get_total
        get_total += month['Days']


def set_first_week(ref_year_twok, get_total):
    """
    Function that sets the days of the first week of the input year to the numerical weekday value.
    The fist argument will be 1 with last being 0, but the positional go 0 - 6 to correlate back to the weekdays list.
    Done by modulus of 7 to determine its remainder meaning the 7th day of week (Sunday) would always be 0.

    Args:
        ref_year_twok: the altered reference year of the first week of year 2000.
        get_total: the total amount of days in the year to the valid input day
    Returns:
        wday_pos: the weekday numerical value
    """
    x = 1
    for weekday in ref_year_twok:
        if weekday['start_days'] and x == 7:
            weekday['start_days'] = 0
        elif weekday['start_days'] and x < 7:
            weekday['start_days'] = x
            x += 1
    for weekday in ref_year_twok:
        if not weekday['start_days'] and x == 7:
            weekday['start_days'] = 0
        elif not weekday['start_days']:
            weekday['start_days'] = x
            x += 1
    wday_pos = None
    for weekday in ref_year_twok:
        if get_total % 7 == weekday['start_days']:
            wday_pos = weekday['position']
    return wday_pos


def calc_first_week(year_scale, reg, leap, ref_year_twok):
    """
    Calculates the first week of the input year.
    Goes the the leap and regular years and changes the monday - sunday bool values respectively.

    Args:
        year_scale: True if year goes above 2000, False if less
        reg: the amount of regular years since 2000
        leap: the amount of leap years since 2000
        ref_year_twok: the reference year of the year 2000
    """
    if not year_scale:
        while reg > 0:
            index = 0
            check_true = False
            for check_days in ref_year_twok:
                if check_days['start_days']:
                    index += 1
            if index == 7:
                for set_days in ref_year_twok:
                    set_days['start_days'] = False
                ref_year_twok[6]['start_days'] = True
                reg -= 1
                check_true = True
            index = 0
            if not check_true:
                for wdays in ref_year_twok:
                    if wdays['start_days']:
                        ref_year_twok[index - 1]['start_days'] = True
                        reg -= 1
                        break
                    index += 1
        while leap > 0:
            index = 0
            check_true = False
            for check_days in ref_year_twok:
                if check_days['start_days']:
                    index += 1
            if index == 6:
                for set_days in ref_year_twok:
                    set_days['start_days'] = False
                ref_year_twok[6]['start_days'] = True
                leap -= 1
                check_true = True
            if index == 7:
                for set_days in ref_year_twok:
                    set_days['start_days'] = False
                ref_year_twok[6]['start_days'] = True
                ref_year_twok[5]['start_days'] = True
                leap -= 1
                check_true = True
            index = 0
            if not check_true:
                for wdays in ref_year_twok:
                    if wdays['start_days']:
                        ref_year_twok[index - 1]['start_days'] = True
                        ref_year_twok[index - 2]['start_days'] = True
                        leap -= 1
                        break
                    index += 1
    if year_scale:
        while reg > 0:
            index = 0
            check_true = False
            for check_days in ref_year_twok:
                if check_days['start_days']:
                    index += 1
            if index == 1:
                for set_days in ref_year_twok:
                    set_days['start_days'] = True
                reg -= 1
                check_true = True
            index = 0
            if not check_true:
                for wdays in ref_year_twok:
                    if wdays['start_days']:
                        ref_year_twok[index]['start_days'] = False
                        reg -= 1
                        break
                    index += 1
        while leap > 0:
            index = 0
            check_true = False
            for check_days in ref_year_twok:
                if check_days['start_days']:
                    index += 1
            if index == 2:
                for set_days in ref_year_twok:
                    set_days['start_days'] = True
                leap -= 1
                check_true = True
            if index == 1:
                for set_days in ref_year_twok:
                    set_days['start_days'] = True
                ref_year_twok[0]['start_days'] = False
                leap -= 1
                check_true = True
            index = 0
            if not check_true:
                for wdays in ref_year_twok:
                    if wdays['start_days']:
                        ref_year_twok[index]['start_days'] = False
                        ref_year_twok[index + 1]['start_days'] = False
                        leap -= 1
                        break
                    index += 1


def leap_year_determination(year):
    """
    Determines of the input year is a leap year.

    Args:
        year: the user input year
    Returns:
        True: the year is a leap
        False: the year is not a leap
    """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


def daylight_savings_calc(start, end, total, daylight_time):
    """
    Determines if the the data states a date in which daylight savings is in effect.
    Goes by days as well as days to determine an accuracy of to the minute.

    Args:
        start: the starting day of daylight savings
        end: the ending day of daylight savings
        total: the users day total
        daylight_time: the users time input, turned into an int for more accurate comparisons
    Returns:
        1: if daylight savings is in effect
        0: if daylight savings is not in effect
    """
    if start < total < end:
        return 1
    elif total == start and daylight_time >= 200:
        return 1
    elif total == end and daylight_time < 200:
        return 1
    return 0


def time_format(arg: tuple = None):
    """
    Formats the time of a custom valid time tuple or current time tuple from the time import.
    Default argument sets localtime tuple to arg to allow further entries with multiple different objects.

    Args:
        arg: a tuple of the date holding information, either custom or from time import
    """
    if arg is None:
        arg = time.localtime()
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    abbreviation = int(str(arg[2])[-1])
    if abbreviation == 1:
        abbreviation = "st"
    elif abbreviation == 2:
        abbreviation = "nd"
    elif abbreviation == 3:
        abbreviation = "rd"
    else:
        abbreviation = "th"
    if arg == 12:
        twelve_time = arg
        m = "PM"
    elif arg[3] == 0:
        twelve_time = 12
        m = "AM"
    elif arg[3] > 12:
        twelve_time = arg[3] - 12
        m = "PM"
    else:
        twelve_time = arg[3]
        m = "AM"
    print(f"\n"f"{arg[2]}/{arg[1]}/{arg[0]}"
          f"\n{weekdays[arg[5 if len(arg) == 8 else 6]]}, {months[arg[1] - 1]} {arg[2]}{abbreviation}"
          f"\n{twelve_time}:{arg[4]} {m}"
          f"\nCurrently {'daylight savings time.' if arg[7 if len(arg) == 8 else 8] == 1 else 'no daylight savings.'}"
          f"\n")


def text_valid(string):
    """
    Validates a string.

    Args:
        string: text to show user
    Returns:
        user: the valid string
    """
    while True:
        user = input(string)
        if user.isalpha():
            return user


def number_valid(string):
    """
    Validates numerical whole number data.

    Args:
        string: text to show user
    Returns:
        int(user): the valid number
    """
    while True:
        user = input(string)
        if user.isdigit():
            return int(user)


def month_check(months, user_month):
    """
    Validates the user month input.
    Error caught if user did not enter a string.

    Args:
        months: dict list of the months and their titles
        user_month: the users input (expected text)
    Returns:
        True: if the user input a month in list
        False: if user did not enter a month name
    """
    for month in months:
        if month["Month"].upper() == user_month.upper():
            return True
    return False


if __name__ == "__main__":
    """
    Runs the program if the file ran is the main file and not an import.
    """
    time_input()
