import re


def is_num_negative(num):
    """ Function #3 Helper Function
    Name: is_num_negative
    Purpose: Returns a True value if the number passed is negative, False
    otherwise
    Precondition: An integer, either pos/neg, passed as a parameter
    Postcondition: A boolean value, reflecting the number's sign, is returned
    to the calling function
    """
    return num < 0


def dec_to_base16(num1):
    """Function #3 Helper Function
    Name: dec_to_base16
    Purpose: Divides an integer into its equivalent base 16 digit (or nibble)
    values, and returns them in a list
    Precondition: An integer passed to the function
    Postcondition: A list of integers, equivalent to the hexadecimal digits
    that comprise the total value of the number passed, returned to the
    calling function
    """
    hex_list = []
    if num1 < 0:
        num1 = num1 * -1
    while num1 >= 16:
        new_mod = int(num1 % 16)
        hex_list.insert(0, new_mod)
        num1 = int(num1 / 16)
    hex_list.insert(0, num1)

    return hex_list


def conv_to_hex_values(hex_list):
    """Function #3 Helper Function
    Name: conv_to_hex_values
    Purpose: Converts integer values into their hexadecimal string equivalents
    and returns them in a list
    Precondition: A list of integer values, each corresponding to a valid
    base 16 value, passed as a parameter
    Postcondition: A list of string values, each corresponding to a
    hexadecimal value returned to the calling function
    """
    hex_dict = {15: 'F', 14: 'E', 13: 'D', 12: 'C', 11: 'B', 10: 'A', 9: '9',
                8: '8',
                7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2', 1: '1', 0: '0'}

    hex_list = [v for i in range(len(hex_list)) for k, v in hex_dict.items()
                if k == hex_list[i]]

    return hex_list


def conv_num():
    """
    Takes a string as input and converts the string into a number and
    returns the number. Returns None if the string is not a valid number
    or if the input is not a string.
    """
    pass


def value_of_char(char):
    """
    Takes a single character of 0-9, A-F, or a-f and returns the
    integer value of that character.
    """
    ascii_value = ord(char.lower())

    # Char is a number
    if ascii_value >= 48 and ascii_value <= 57:
        return ascii_value - 48

    # Char is a letter
    return ascii_value - 87


def convert_integral_part(num_str, base=10):
    """
    Takes a string representing a positive non-fractional number as input
    and converts and returns the string as an integer.
    """
    return sum(
        value_of_char(char) * base**power
        for power, char in enumerate(reversed(num_str))
    )


def convert_fractional_part(num_str):
    """
    Takes a string representing the fractional part of a number as input and
    converts and returns the string as a float. (e.g. '945' returns 0.945)
    """
    return convert_integral_part(num_str) / 10**len(num_str)


def valid_number(num_str):
    """
    Takes a string as input and returns 'integer' if the string is a valid
    integer, 'decimal' if the string is a valid decimal number, or
    'hexadecimal' if the string is a valid hexadecimal number.
    Returns False otherwise.
    """
    if valid_integer(num_str):
        return 'integer'

    if valid_decimal(num_str):
        return 'decimal'

    if valid_hexadecimal(num_str):
        return 'hexadecimal'

    return False


def valid_integer(num_str):
    """
    Takes a string as input and returns True if the string represents a valid
    integer. Returns False otherwise.
    """
    match = re.match(r'^-?[0-9]+$', num_str)
    return match is not None


def valid_decimal(num_str):
    """
    Takes a string as input and returns True if the string represents a valid
    decimal number. Returns False otherwise.
    """
    match = re.match(r'^(?=.*?[0-9])-?[0-9]*\.[0-9]*$', num_str)
    return match is not None


def valid_hexadecimal(num_str):
    """
    Takes a string as input and returns True if the string represents a valid
    hexadecimal number. Returns False otherwise.
    """
    match = re.match(r'^-?0[xX][0-9a-fA-F]*$', num_str)
    return match is not None


##########
# Helper functions for my_datetime() function
##########

def get_full_date(month, day, yr):
    """
    For output use.
    Input: A month, day, and year in integer form

    Output: Converts the input into
    the proper string for output.
    """
    temp_date = str(month) + "-"

    # Adding a 0 if the month number is less than 10, i.e. May would be 05
    if month < 10:
        temp_date = "0" + temp_date

    # Adding a 0 if the day number is less than 10, i.e. the 5th would be 05
    if day < 10:
        temp_date += "0"

    temp_date = temp_date + str(day) + "-" + str(yr)

    return temp_date


# Getting number of days from seconds in a day
def get_days(num_sec):
    """
    Input: Number of seconds

    Output: Number of days based off input
    """
    # Seconds in a day
    seconds = 86400
    days = 0

    while num_sec >= seconds:
        num_sec -= seconds
        days += 1

    return days


# Getting amount years and days left over from an input of days
# Code cited from: https://www.geeksforgeeks.org/program-convert-
# given-number-days-terms-years-weeks-days/
def get_years(days):
    """
    Input: a number of days

    Output: Number of years and days left over
    (i.e. input of 366 days = output of 1 year, 1 day)
    """
    if days >= 365:
        years = int(days / 365)
        days_left = (days % 365) % 7
        return years, days_left

    else:
        return 0, days


# Getting specific date from epoch date based on input of years and days
# https://www.epochconverter.com/
def get_date_from_epoch(years, days):
    """
    Input: A number of years and number of days

    Output: The specific date from the epoch (1/1/1970)
    based on input years and days.
    (i.e. an input of 10 years, 50 days will return the specific date
    of 10 years and 50 days from 1/1/1970)
    """
    # Making lists for days in each month for leap years and regular years
    leapyear_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cur_day = 1
    cur_month = 1
    # Epoch year
    cur_year = 1970 + years

    while days:
        cal = month_days
# https://en.wikipedia.org/wiki/Leap_year
# If a year is exactly divisible by 4, it is a leap year
# It is also a leap year if it exactly divisible by exactly 100 and 400 as well
        if cur_year % 4 == 0:
            cal = leapyear_days

        elif cur_year % 400 == 0:
            cal = month_days

        elif cur_year % 100 == 0:
            cal = leapyear_days

        if cur_day == cal[cur_month-1]:
            cur_month += 1
            # Signals end of the year
            if cur_month == 13:
                cur_month = 1
                cur_year += 1

            cur_day = 0
        cur_day += 1
        days -= 1

    return cur_month, cur_day, cur_year
