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

    # Test Function #3 dec_to_base16 7: Pass the smallest 32-bit int to
    # make sure it is treated correctly
    def test7(self):
        input1 = -2147483647
        expected = [7, 15, 15, 15, 15, 15, 15, 15]
        self.assertEqual(task.dec_to_base16(input1), expected,
                         msg='Expected {} got {}'.format(expected,
                                                         task.dec_to_base16
                                                         (input1)))


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


if __name__ == '__main__':
    unittest.main(verbosity=2)
