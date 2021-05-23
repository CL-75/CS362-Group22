import unittest
import task


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


# Test class for get_years() function. Tests input and expected output.
class TestGetYears(unittest.TestCase):

    def test_1(self):
        data = 365
        expected = 1.0, 365
        self.assertEqual(task.get_years(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_years(data)))

    def test_2(self):
        data = 912.5
        expected = 2.5, 912.5
        self.assertEqual(task.get_years(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_years(data)))

    def test_3(self):
        data = 3650
        expected = 10.0, 3650
        self.assertEqual(task.get_years(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_years(data)))

    def test_4(self):
        data = 18250
        expected = 50.0, 18250
        self.assertEqual(task.get_years(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_years(data)))

    def test_5(self):
        data = 0
        expected = 0.0, 0
        self.assertEqual(task.get_years(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_years(data)))

    def test_6(self):
        data = 18250000
        expected = 50000.0, 18250000
        self.assertEqual(task.get_years(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_years(data)))

    def test_7(self):
        data = 20
        expected = 0.1, 20
        self.assertEqual(task.get_years(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_years(data)))

    def test_8(self):
        data = 15622
        expected = 42.8, 15622
        self.assertEqual(task.get_years(data), expected,
                         msg='expected {} got {}'.format(expected,
                         task.get_years(data)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
