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
        hex_list.append(new_mod)
        num1 = int(num1 / 16)
    hex_list.append(num1)
    hex_list = hex_list[::-1]

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
    intger value of that character.
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
    Converts the given month, day, and year into
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
