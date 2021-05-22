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
