import unittest
import task


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


# Tests for get_full_date() function. Tests output.
class TestGetFullDate(unittest.TestCase):

    def test_1(self):
        self.assertTrue(task.get_full_date(0, 0, 0), True)

    def test_2(self):
        self.assertTrue(task.get_full_date(10, 27, 2020), True)

    def test_3(self):
        self.assertTrue(task.get_full_date(6, 30, 1995), True)

    def test_4(self):
        self.assertTrue(task.get_full_date(11, 18, 1980), True)

    def test_5(self):
        self.assertTrue(task.get_full_date(1, 1, 1695), True)

    def test_6(self):
        self.assertTrue(task.get_full_date(7, 5, 1991), True)


if __name__ == '__main__':
    unittest.main()
