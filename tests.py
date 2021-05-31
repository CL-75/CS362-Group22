# ---------------------------------------------------------------------------
# Program: tests.py
# Class: CS 362
# Module: Continuous Integration and Code Review
# Assignment: Group Project: Part 2
# Date: June 1, 2021
# Group: 22
# Authors: Jay Chaudhry, Casey Levy, Michael Kistler
# ---------------------------------------------------------------------------
import unittest
import task
import random


# ---------------------------------------------------------------------------
# Function #1 Testing for conv_num()
# Author: Michael Kistler
# ---------------------------------------------------------------------------
# Function #1 Random Testing for conv_num()
class TestConvNumRandom(unittest.TestCase):
    pass


# Function for building random test cases
def build_test_func1(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result,
                         message.format(test_case, expected, result))

    return test


def generate_conv_num_test_cases(tests_to_generate=1000):
    for _ in range(tests_to_generate):
        num_type = random.choice(['integer', 'decimal', 'hexadecimal'])
        num = random.randint(0, 1000000)
        is_negative = random.choice([True, False])
        if num_type == 'integer':
            num_str = str(num)
        elif num_type == 'hexadecimal':
            num_str = hex(num)
        else:
            num += random.randint(0, 9999) / 10000
            num_str = str(num)
        if is_negative:
            num_str = '-' + num_str
            num *= -1
        msg = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func1(num, num_str, task.conv_num, msg)
        setattr(TestConvNumRandom, f'test_{num_str}', new_test)


# Function #1 Testing for conv_num() function
class TestConvNum(unittest.TestCase):
    def test1(self):
        num = ''
        self.assertIsNone(task.conv_num(num))

    def test2(self):
        num = '0'
        self.assertEqual(task.conv_num(num), 0)
        self.assertIsInstance(task.conv_num(num), int)

    def test3(self):
        num = '.0'
        self.assertEqual(task.conv_num(num), 0.0)
        self.assertIsInstance(task.conv_num(num), float)

    def test4(self):
        num = '0x0'
        self.assertEqual(task.conv_num(num), 0)
        self.assertIsInstance(task.conv_num(num), int)

    def test5(self):
        num = '.0.'
        self.assertIsNone(task.conv_num(num))

    def test6(self):
        num = 'F0'
        self.assertIsNone(task.conv_num(num))

    def test7(self):
        num = 0
        self.assertIsNone(task.conv_num(num))

    def test8(self):
        num = '1000'
        self.assertEqual(task.conv_num(num), 1000)
        self.assertIsInstance(task.conv_num(num), int)

    def test9(self):
        num = '1000.99'
        self.assertEqual(task.conv_num(num), 1000.99)
        self.assertIsInstance(task.conv_num(num), float)

    def test10(self):
        num = '0X3e8'
        self.assertEqual(task.conv_num(num), 1000)
        self.assertIsInstance(task.conv_num(num), int)

    def test11(self):
        num = '-5297'
        self.assertEqual(task.conv_num(num), -5297)
        self.assertIsInstance(task.conv_num(num), int)

    def test12(self):
        num = '-6467.185'
        self.assertEqual(task.conv_num(num), -6467.185)
        self.assertIsInstance(task.conv_num(num), float)

    def test13(self):
        num = '-0xd8B7'
        self.assertEqual(task.conv_num(num), -55479)
        self.assertIsInstance(task.conv_num(num), int)

    def test14(self):
        num = '10.'
        self.assertEqual(task.conv_num(num), 10.0)
        self.assertIsInstance(task.conv_num(num), float)

    def test15(self):
        num = '-.87'
        self.assertEqual(task.conv_num(num), -0.87)
        self.assertIsInstance(task.conv_num(num), float)


# Function #1 Testing for convert_integral_part() function
class TestConvertIntegeralPart(unittest.TestCase):
    def test1(self):
        num = '6'
        self.assertEqual(task.convert_integral_part(num), 6)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test2(self):
        num = '72456'
        self.assertEqual(task.convert_integral_part(num), 72456)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test3(self):
        num = '0'
        self.assertEqual(task.convert_integral_part(num), 0)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test4(self):
        num = '10'
        self.assertEqual(task.convert_integral_part(num), 10)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test5(self):
        num = '10'
        self.assertEqual(task.convert_integral_part(num, base=16), 16)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test6(self):
        num = 'A'
        self.assertEqual(task.convert_integral_part(num, base=16), 10)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test7(self):
        num = '63b5e'
        self.assertEqual(task.convert_integral_part(num, base=16), 408414)
        self.assertIsInstance(task.convert_integral_part(num), int)


# Function #1 Testing for convert_fractional_part() function
class TestConvertFractionalPart(unittest.TestCase):
    def test1(self):
        num = '945'
        self.assertEqual(task.convert_fractional_part(num), 0.945)
        self.assertIsInstance(task.convert_fractional_part(num), float)

    def test2(self):
        num = '078'
        self.assertEqual(task.convert_fractional_part(num), 0.078)
        self.assertIsInstance(task.convert_fractional_part(num), float)

    def test3(self):
        num = '400'
        self.assertEqual(task.convert_fractional_part(num), 0.4)
        self.assertIsInstance(task.convert_fractional_part(num), float)

    def test4(self):
        num = '0'
        self.assertEqual(task.convert_fractional_part(num), 0.0)
        self.assertIsInstance(task.convert_fractional_part(num), float)


# Function #1 Testing for valid_number() function
class TestValidNumber(unittest.TestCase):
    def test1(self):
        num = ''
        self.assertEqual(task.valid_number(num), False)

    def test2(self):
        num = '61'
        self.assertEqual(task.valid_number(num), 'integer')

    def test3(self):
        num = '73.72'
        self.assertEqual(task.valid_number(num), 'decimal')

    def test4(self):
        num = '-0x5D8'
        self.assertEqual(task.valid_number(num), 'hexadecimal')

    def test5(self):
        num = '0x67.fa'
        self.assertEqual(task.valid_number(num), False)


# Function #1 Testing for valid_integer() function
class TestValidInteger(unittest.TestCase):
    def test1(self):
        num = ''
        self.assertEqual(task.valid_integer(num), False)

    def test2(self):
        num = '1'
        self.assertEqual(task.valid_integer(num), True)

    def test3(self):
        num = '2'
        self.assertEqual(task.valid_integer(num), True)

    def test4(self):
        num = 'T'
        self.assertEqual(task.valid_integer(num), False)

    def test5(self):
        num = '-15'
        self.assertEqual(task.valid_integer(num), True)

    def test6(self):
        num = '1643'
        self.assertEqual(task.valid_integer(num), True)

    def test7(self):
        num = '436-15'
        self.assertEqual(task.valid_integer(num), False)


# Function #1 Testing for valid_decimal() function
class TestValidDecimal(unittest.TestCase):
    def test1(self):
        num = '.'
        self.assertEqual(task.valid_decimal(num), False)

    def test2(self):
        num = '56'
        self.assertEqual(task.valid_decimal(num), False)

    def test3(self):
        num = '127.54'
        self.assertEqual(task.valid_decimal(num), True)

    def test4(self):
        num = '-36.7'
        self.assertEqual(task.valid_decimal(num), True)

    def test5(self):
        num = '.98'
        self.assertEqual(task.valid_decimal(num), True)

    def test6(self):
        num = '17.'
        self.assertEqual(task.valid_decimal(num), True)

    def test7(self):
        num = '14.87.'
        self.assertEqual(task.valid_decimal(num), False)

    def test8(self):
        num = ''
        self.assertEqual(task.valid_decimal(num), False)


# Function #1 Testing for valid_hexadecimal() function
class TestValidHexadecimal(unittest.TestCase):
    def test1(self):
        num = ''
        self.assertEqual(task.valid_hexadecimal(num), False)

    def test2(self):
        num = '165'
        self.assertEqual(task.valid_hexadecimal(num), False)

    def test3(self):
        num = '0x61F'
        self.assertEqual(task.valid_hexadecimal(num), True)

    def test4(self):
        num = '0x61Y'
        self.assertEqual(task.valid_hexadecimal(num), False)

    def test5(self):
        num = '-0x2b'
        self.assertEqual(task.valid_hexadecimal(num), True)

    def test6(self):
        num = 'x62'
        self.assertEqual(task.valid_hexadecimal(num), False)

    def test7(self):
        num = '-0xFDE5'
        self.assertEqual(task.valid_hexadecimal(num), True)

    def test8(self):
        num = '-0X2b'
        self.assertEqual(task.valid_hexadecimal(num), True)

    def test9(self):
        num = '0x0'
        self.assertEqual(task.valid_hexadecimal(num), True)


# ---------------------------------------------------------------------------
# Function #2 Testing for my_datetime()
# Author: Casey Levy
# ---------------------------------------------------------------------------
# Tests for get_full_date() function. Tests output.
class TestGetFullDate(unittest.TestCase):

    def test_1(self):
        month = 0
        day = 0
        yr = 0
        expected = '00-00-0'
        self.assertEqual(task.get_full_date(month, day, yr), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_full_date(month, day, yr)))

    def test_2(self):
        month = 10
        day = 27
        yr = 2020
        expected = '10-27-2020'
        self.assertEqual(task.get_full_date(month, day, yr), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_full_date(month, day, yr)))

    def test_3(self):
        month = 6
        day = 30
        yr = 2019
        expected = '06-30-2019'
        self.assertEqual(task.get_full_date(month, day, yr), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_full_date(month, day, yr)))

    def test_4(self):
        month = 11
        day = 18
        yr = 1995
        expected = '11-18-1995'
        self.assertEqual(task.get_full_date(month, day, yr), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_full_date(month, day, yr)))

    def test_5(self):
        month = 1
        day = 1
        yr = 1695
        expected = '01-01-1695'
        self.assertEqual(task.get_full_date(month, day, yr), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_full_date(month, day, yr)))

    def test_6(self):
        month = 7
        day = 5
        yr = 1991
        expected = '07-05-1991'
        self.assertEqual(task.get_full_date(month, day, yr), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_full_date(month, day, yr)))


# Tests for get_days() function. Tests proper number of days is printed
#  based on input in seconds.
class TestGetDays(unittest.TestCase):

    def test_1(self):
        data = 172800
        expected = 2
        self.assertEqual(task.get_days(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_days(data)))

    def test_2(self):
        data = 0
        expected = 0
        self.assertEqual(task.get_days(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_days(data)))

    def test_3(self):
        data = 31540000
        expected = 365
        self.assertEqual(task.get_days(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_days(data)))

    def test_4(self):
        data = 604800
        expected = 7
        self.assertEqual(task.get_days(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_days(data)))

    def test_5(self):
        data = 8640000
        expected = 100
        self.assertEqual(task.get_days(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_days(data)))

    def test_6(self):
        data = 86400000
        expected = 1000
        self.assertEqual(task.get_days(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_days(data)))

    def test_7(self):
        data = 90000
        expected = 1
        self.assertEqual(task.get_days(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_days(data)))


# Tests for get_date_from_epoch() function. Tests input and expected output.
class TestGetDateFromEpoch(unittest.TestCase):

    def test_1(self):
        years = 0
        days = 0
        expected = 1, 1, 1970
        self.assertEqual(task.get_date_from_epoch(years, days), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_date_from_epoch(years, days)))

    def test_2(self):
        years = 500
        days = 30
        expected = 1, 31, 2470
        self.assertEqual(task.get_date_from_epoch(years, days), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_date_from_epoch(years, days)))

    def test_3(self):
        years = 5
        days = 700
        expected = 12, 1, 1976
        self.assertEqual(task.get_date_from_epoch(years, days), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_date_from_epoch(years, days)))

    def test_4(self):
        years = 6004
        days = 291
        expected = 10, 19, 7974
        self.assertEqual(task.get_date_from_epoch(years, days), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_date_from_epoch(years, days)))

    def test_5(self):
        years = 1
        days = 1000
        expected = 9, 27, 1973
        self.assertEqual(task.get_date_from_epoch(years, days), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_date_from_epoch(years, days)))

    def test_6(self):
        years = 0
        days = 9578
        expected = 3, 23, 1996
        self.assertEqual(task.get_date_from_epoch(years, days), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_date_from_epoch(years, days)))

    def test_7(self):
        years = 234
        days = 183
        expected = 7, 2, 2204
        self.assertEqual(task.get_date_from_epoch(years, days), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_date_from_epoch(years, days)))

    def test_8(self):
        years = 374
        days = 542
        expected = 6, 26, 2345
        self.assertEqual(task.get_date_from_epoch(years, days), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_date_from_epoch(years, days)))


# Tests for main function, my_datetime().
class TestMyDateTime(unittest.TestCase):

    def test_1(self):
        time = 0
        self.assertEqual(task.my_datetime(time), '01-01-1970')

    def test_2(self):
        time = 123456789
        self.assertEqual(task.my_datetime(time), '11-29-1973')

    def test_3(self):
        time = 987654321
        self.assertEqual(task.my_datetime(time), '04-19-2001')

    def test_4(self):
        time = 856320457
        self.assertEqual(task.my_datetime(time), '02-19-1997')

    def test_5(self):
        time = 753951204
        expected = '11-22-1993'
        self.assertEqual(task.my_datetime(time), expected)

    def test_6(self):
        time = 20
        expected = '01-01-1970'
        self.assertEqual(task.my_datetime(time), expected)

    def test_7(self):
        time = 100000
        expected = '01-02-1970'
        self.assertEqual(task.my_datetime(time), expected)

    def test_8(self):
        time = 357456208
        expected = '04-30-1981'
        self.assertEqual(task.my_datetime(time), expected)

    def test_9(self):
        time = 2345773421
        expected = '05-02-2044'
        self.assertEqual(task.my_datetime(time), expected)

    def test_10(self):
        time = 657403582
        expected = '10-31-1990'
        self.assertEqual(task.my_datetime(time), expected)

    def test_11(self):
        time = 83240652
        expected = '08-21-1972'
        self.assertEqual(task.my_datetime(time), expected)

    def test_12(self):
        time = 1583032258
        expected = '03-01-2020'
        self.assertEqual(task.my_datetime(time), expected)

    def test_13(self):
        time = 99999999
        expected = '03-03-1973'
        self.assertEqual(task.my_datetime(time), expected)

    def test_14(self):
        time = 111111111
        expected = '07-10-1973'
        self.assertEqual(task.my_datetime(time), expected)

    def test_15(self):
        time = 678749722
        expected = '07-05-1991'
        self.assertEqual(task.my_datetime(time), expected)

    def test_16(self):
        time = 665928000
        expected = '02-07-1991'
        self.assertEqual(task.my_datetime(time), expected)

    def test_17(self):
        time = 1530376340
        expected = '06-30-2018'
        self.assertEqual(task.my_datetime(time), expected)

    def test_18(self):
        time = 1574078700
        expected = '11-18-2019'
        self.assertEqual(task.my_datetime(time), expected)

    def test_19(self):
        time = 129900
        expected = '01-02-1970'
        self.assertEqual(task.my_datetime(time), expected)

    def test_20(self):
        time = 1640419200
        expected = '12-25-2021'
        self.assertEqual(task.my_datetime(time), expected)


# ---------------------------------------------------------------------------
# Function #3 Testing for conv_endian()
# Author: Jay Chaudhry
# ---------------------------------------------------------------------------
# Function #3 Testing for is_num_negative() Function
class TestIsNumNegative(unittest.TestCase):
    # Test Function #3 is_num_negative 1: Test 0
    def test1(self):
        input1 = 0
        self.assertFalse(task.is_num_negative(input1))

    # Test Function #3 is_num_negative 2: Test -1
    def test2(self):
        input1 = -1
        self.assertTrue(task.is_num_negative(input1))

    # Test Function #3 is_num_negative 3: Test 1
    def test3(self):
        input1 = 1
        self.assertFalse(task.is_num_negative(input1))

    # Test Function #3 is_num_negative 4: Test smallest 32-bit negative int
    def test4(self):
        input1 = -2147483648
        self.assertTrue(task.is_num_negative(input1))

    # Test Function #3 is_num_negative 5: Test largest 32-bit positive int
    def test5(self):
        input1 = 2147483647
        self.assertFalse(task.is_num_negative(input1))


# Function #3 Testing for dec_to_base16() Function
class TestDecToBase16(unittest.TestCase):
    # Test Function #3 dec_to_binary 1: Pass zero to make sure it is
    # handled correctly
    def test1(self):
        input1 = 0
        expected = [0]
        self.assertEqual(task.dec_to_base16(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.dec_to_base16
                                                         (input1)))

    # Test Function #3 dec_to_base16 2: Pass the largest hex digit value
    # to see that it is stored correctly
    def test2(self):
        input1 = 15
        expected = [15]
        self.assertEqual(task.dec_to_base16(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.dec_to_base16
                                                         (input1)))

    # Test Function #3 dec_to_base16 3: Pass an int value one larger than
    # the largest hex digit to see that it is stored correctly
    def test3(self):
        input1 = 16
        expected = [1, 0]
        self.assertEqual(task.dec_to_base16(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.dec_to_base16
                                                         (input1)))

    # Test Function #3 dec_to_base16 4: Pass a value one greater than the
    # 16s column to make sure that it is handled correctly
    def test4(self):
        input1 = 256
        expected = [1, 0, 0]
        self.assertEqual(task.dec_to_base16(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.dec_to_base16
                                                         (input1)))

    # Test Function # dec_to_base16 5: Pass lecture example integer
    def test5(self):
        input1 = 954786
        expected = [14, 9, 1, 10, 2]
        self.assertEqual(task.dec_to_base16(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.dec_to_base16
                                                         (input1)))

    # Test Function #3 dec_to_base16 6: Pass largest 32-bit int to make
    # sure it is handled correctly
    def test6(self):
        input1 = 2147483647
        expected = [7, 15, 15, 15, 15, 15, 15, 15]
        self.assertEqual(task.dec_to_base16(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.dec_to_base16
                                                         (input1)))

    # Test Function #3 dec_to_base16 7: Pass the smallest 32-bit int,
    # plus one, to make sure it is treated correctly
    def test7(self):
        input1 = -2147483647
        expected = [7, 15, 15, 15, 15, 15, 15, 15]
        self.assertEqual(task.dec_to_base16(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.dec_to_base16
                                                         (input1)))


# Function #3 Testing for conv_to_hex_values() Function
class TestConvDecToHexValues(unittest.TestCase):
    # Test Function #3 conv_to_hex_values 1: Pass a list of zeros to
    # make sure that each value is formatted correctly
    def test1(self):
        input1 = [0, 0, 0, 0, 0]
        expected = ['0', '0', '0', '0', '0']
        self.assertEqual(task.conv_to_hex_values(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.
                                                         conv_to_hex_values
                                                         (input1)))

    # Test Function #3 conv_to_hex_values 2: Pass a list of values 1-9
    # to make sure that each value is converted correctly
    def test2(self):
        input1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.assertEqual(task.conv_to_hex_values(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.
                                                         conv_to_hex_values
                                                         (input1)))

    # Test Function #3 conv_to_hex_values 2: Pass a list of the highest
    # base 16 digit values, in reverse order, to make sure that  each
    # value is converted correctly
    def test3(self):
        input1 = [15, 14, 13, 12, 11, 10]
        expected = ['F', 'E', 'D', 'C', 'B', 'A']
        self.assertEqual(task.conv_to_hex_values(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.
                                                         conv_to_hex_values
                                                         (input1)))

    # Test Function #3 conv_to_hex_values 3: Pass a list of
    # equivalent hex values, that represent the largest possible
    # 32-bit integer, to make sure that each value is converted correctly
    def test4(self):
        input1 = [7, 15, 15, 15, 15, 15, 15, 15]
        expected = ['7', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
        self.assertEqual(task.conv_to_hex_values(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.
                                                         conv_to_hex_values
                                                         (input1)))

    # Test Function #3 conv_to_hex_values: Pass a list of hex values,
    # corresponding to the lecture example, to make sure that each value
    # is converted correctly
    def test5(self):
        input1 = [14, 9, 1, 10, 2]
        expected = ['E', '9', '1', 'A', '2']
        self.assertEqual(task.conv_to_hex_values(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_to_hex_values
                                                         (input1)))


# Function #3 testing for pad_hex_list()
class TestPadHexList(unittest.TestCase):
    # Pass a list with one value to make sure the list is padded correctly
    def test1(self):
        input1 = ['0']
        expected = ['0', '0']
        self.assertEqual(task.pad_hex_list(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         pad_hex_list
                                                         (input1)))

    def test2(self):
        # Pass a list with an even number of values to make sure the list
        # is left untouched
        input1 = ['0', '0']
        expected = ['0', '0']
        self.assertEqual(task.pad_hex_list(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         pad_hex_list
                                                         (input1)))

    def test3(self):
        # Pass a list of hex string values equivalent to the largest
        # 32-bit int to make sure it is handled correctly
        input1 = ['7', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
        expected = ['7', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
        self.assertEqual(task.pad_hex_list(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         pad_hex_list
                                                         (input1)))

    def test4(self):
        # Pass a list of values corresponding to the lecture example to
        # make sure it is padded correctly
        input1 = ['E', '9', '1', 'A', '2']
        expected = ['0', 'E', '9', '1', 'A', '2']
        self.assertEqual(task.pad_hex_list(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         pad_hex_list
                                                         (input1)))


# Function #3 Testing for format_hex_list()
class TestFormatHexList(unittest.TestCase):
    # Pass a list containing two hex digit string values to make sure
    # that they are formatted correctly into one byte value
    def test1(self):
        input1 = ['0', '0']
        expected = ['00']
        self.assertEqual(task.format_hex_list(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         format_hex_list
                                                         (input1)))

    # Pass a list containing four hex digit string values to make sure
    # that they are formatted correctly into two byte values
    def test2(self):
        input1 = ['2', '3', '7', '8']
        expected = ['23', '78']
        self.assertEqual(task.format_hex_list(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         format_hex_list
                                                         (input1)))

    # Pass a list containing hex digit, string values, equivalent to the
    # largest 32-bit pos integer, to make sure that they are formatted
    # correctly
    def test3(self):
        input1 = ['7', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
        expected = ['7F', 'FF', 'FF', 'FF']
        self.assertEqual(task.format_hex_list(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         format_hex_list
                                                         (input1)))

    # Pass a list containing hex digit, string values, equivalent to the
    # big endian lecture example, to make sure that they are formatted
    # correctly
    def test4(self):
        input1 = ['0', 'E', '9', '1', 'A', '2']
        expected = ['0E', '91', 'A2']
        self.assertEqual(task.format_hex_list(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         format_hex_list
                                                         (input1)))

    # Pass a list containing hex digit, string values, equivalent to the
    # little endian lecture example, to make sure that they are formatted
    # correctly
    def test5(self):
        input1 = ['A', '2', '9', '1', '0', 'E']
        expected = ['A2', '91', '0E']
        self.assertEqual(task.format_hex_list(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         format_hex_list
                                                         (input1)))


# Testing for Function #3 conv_endian()
class TestConvEndian(unittest.TestCase):
    def test1(self):
        # Pass in zero to make sure that the correct string value is returned
        input1 = 0
        expected = '00'
        self.assertEqual(task.conv_endian(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_endian
                                                         (input1)))

    def test2(self):
        # Pass in value with no byte order string to make sure the correct
        # string value is returned
        input1 = 954786
        expected = '0E 91 A2'
        self.assertEqual(task.conv_endian(input1), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_endian
                                                         (input1)))

    def test3(self):
        # Pass in value with explicit byte order of 'big' to make sure the
        # correct string value is returned
        input1 = 954786
        input2 = 'big'
        expected = '0E 91 A2'
        self.assertEqual(task.conv_endian(input1, input2), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_endian
                                                         (input1, input2)))

    def test4(self):
        # Pass in value with explicit byte order of 'little' passed, to
        # make sure the correct string value is returned
        input1 = 954786
        input2 = 'little'
        expected = 'A2 91 0E'
        self.assertEqual(task.conv_endian(input1, input2), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_endian
                                                         (input1, input2)))

    def test5(self):
        # Pass in negative value with explicit 'big' byte order to
        # make sure the correct string is returned
        input1 = -954786
        input2 = 'big'
        expected = '-0E 91 A2'
        self.assertEqual(task.conv_endian(input1, input2), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_endian
                                                         (input1, input2)))

    def test6(self):
        # Pass negative value, with 'little' byte order string, as
        # parameters to make sure the correct string is returned
        input1 = -954786
        input2 = 'little'
        expected = '-A2 91 0E'
        self.assertEqual(task.conv_endian(input1, input2), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_endian
                                                         (input1, input2)))

    def test7(self):
        # Pass in value with an invalid byte order string to make
        # sure None is returned
        input1 = 954786
        input2 = 'small'
        expected = None
        self.assertEqual(task.conv_endian(input1, input2), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_endian
                                                         (input1, input2)))

    def test8(self):
        # Pass in value, but with another invalid byte order string,
        # to make sure it returns None
        input1 = 20
        input2 = 'itty-bitty'
        expected = None
        self.assertEqual(task.conv_endian(input1, input2), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_endian
                                                         (input1, input2)))

    def test9(self):
        # Pass the largest 32-bit value to make sure that is returned
        # correctly in little endian order
        input1 = 2147483647
        input2 = 'little'
        expected = 'FF FF FF 7F'
        self.assertEqual(task.conv_endian(input1, input2), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_endian
                                                         (input1, input2)))

    def test10(self):
        # Pass a negative value to make sure that the resulting hex string
        # is padded with the requisite leading zero
        input1 = -120220722
        input2 = 'big'
        expected = '-07 2A 6C 32'
        self.assertEqual(task.conv_endian(input1, input2), expected,
                         msg='Expected {} got {}'.format(expected, task.
                                                         conv_endian
                                                         (input1, input2)))


# Function #3 Dynamic Random Testing Class
class TestFunc3Random(unittest.TestCase):
    pass


# Function #3 dynamic random testing function
def build_test_func3(expected, test_case, order, func_under_test, message):
    def test(self):
        result = func_under_test(test_case, order)
        self.assertEqual(expected, result, message.format(test_case,
                                                          expected, result))

    return test


# Helper Function for random_hex_values
# Determines is random integer is pos or neg
# and returns the bool value
def is_num_neg(num1):
    return num1 < 0


# Helper Function for random_hex_values
# Removes unwanted chars after hex method is
# called on random integer value
def remove_chars(hex_val):
    if hex_val[0] == '-':
        hex_val = hex_val.replace('-', '')
    if len(hex_val) % 2 != 0:
        hex_val = '0' + hex_val

    return hex_val


# Helper Function for random_hex_values
# formats hex value string to compare expected results with
# output from conv_endian
def format_final_str(hex_val):
    final_str = ""
    # count = 0
    for n in range(len(hex_val)):
        if n > 0 and n % 2 == 0:
            final_str = final_str + ' '
        final_str = final_str + hex_val[n]
        # count += 1

    return final_str


# Generates 10000 random integers and calculates expected hex values,
# alternating byte order with each test, to test and verify
# the output of function #3
def random_hex_values(tests_to_gen=10000):
    for i in range(tests_to_gen):
        # Alternate byte order after each test
        if i % 2 == 0:
            input2 = 'big'
        else:
            input2 = 'little'
        rand_int = random.randint(-2147483647, 2147483647)
        is_negative = is_num_neg(rand_int)
        hex_val = format(rand_int, 'X')
        hex_val = str(hex_val)
        hex_val = remove_chars(hex_val)
        final_str = format_final_str(hex_val)
        # reverse byte order if necessary
        if input2 == 'little':
            list1 = final_str.split()
            list1 = list1[::-1]
            final_str = ' '.join([i for i in list1])
        # add minus sign to any negative numbers
        if is_negative:
            final_str = '-' + final_str
        input1 = rand_int
        expected = final_str
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func3(expected, input1, input2, task.conv_endian,
                                    message)
        setattr(TestFunc3Random, 'test_{}_{}'.format(input1, input2), new_test)


if __name__ == '__main__':
    random_hex_values()
    generate_conv_num_test_cases()
    unittest.main(verbosity=2)
