import re


def conv_num(num_str):
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

def get_str(month, day, yr):
    temp_date = str(month) + "-"

    if month < 10:
        temp_date = "0" + temp_date

    if day < 10:
        temp_date += "0"

    temp_date = temp_date + str(day) + "-" + str(yr)

    return temp_date
