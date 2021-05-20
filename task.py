import re


def conv_num(num_str):
    """
    Takes a string as input and converts the string into a number and
    returns the number. Returns False if the string is not a valid number.
    """
    pass


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
    match = re.match(r'^-?0x[0-9a-fA-F]*$', num_str)
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
